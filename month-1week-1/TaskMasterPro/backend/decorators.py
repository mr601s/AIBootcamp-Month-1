"""
Professional decorators for TaskMasterPro
Day 15 concepts applied to production application
"""

import time
import functools
from datetime import datetime
import json
import os


class AppDecorators:
    """Reusable decorators for task management"""

    # Log files
    LOG_DIR = os.path.join(os.path.dirname(__file__), 'data')
    ACTIVITY_LOG = os.path.join(LOG_DIR, 'activity.log')
    PERFORMANCE_LOG = os.path.join(LOG_DIR, 'performance.log')

    @staticmethod
    def ensure_log_dir():
        """Ensure log directory exists"""
        os.makedirs(AppDecorators.LOG_DIR, exist_ok=True)

    @staticmethod
    def timer(func):
        """Measure and log execution time"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            duration = end - start

            # Log to performance file
            AppDecorators.ensure_log_dir()
            perf_entry = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'function': func.__name__,
                'duration_seconds': duration
            }

            try:
                with open(AppDecorators.PERFORMANCE_LOG, 'a') as f:
                    f.write(json.dumps(perf_entry) + '\n')
            except:
                pass

            # Print if slow
            if duration > 0.1:
                print(f'⚠️ Function "{func.__name__}" took {duration:.4f} seconds')

            return result
        return wrapper
    
    @staticmethod
    def audit_log(action_type, include_result=False):
            """Log all actions for audit trail"""
            def decorator(func):
                @functools.wraps(func)
                def wrapper(*args, **kwargs):
                    timestamp = datetime.now().isoformat()

                    # Execute function
                    result = func(*args, **kwargs)

                    # Build log entry
                    log_entry = {
                        'timestamp': timestamp,
                        'action': action_type,
                        'function': func.__name__,
                        'success': result is not False and result is not None
                    }

                    if include_result and result:
                        log_entry['result'] = str(result)[:100] # truncate long results 

                    # Append to log file
                    AppDecorators.ensure_log_dir()
                    try:
                        with open(AppDecorators.ACTIVITY_LOG, 'a') as f:
                            f.write(json.dumps(log_entry) + '\n')
                    except Exception as e:
                        print(f'Logging error: {e}')

                    return result
                return wrapper
            return decorator
        
    @staticmethod
    def cache_with_ttl(ttl_minutes=30):
        """Cache results with time-to-live"""
        cache = {}

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # Create cache key from arguments
                cache_key = f'{func.__name__}: {str(args)}:{str(kwargs)}'
                now = time.time()

                # Check cache
                if cache_key in cache:
                    cached_time, cached_data = cache[cache_key]
                    age_minutes = (now - cached_time) / 60

                    if age_minutes < ttl_minutes:
                        print(f'🔄 Using cached result for "{func.__name__}"')
                        return cached_data
                    else:
                        # Expired
                        del cache[cache_key]

                # Fetch fresh data
                print(f'🔄 Cache miss for {func.__name__}, fetching fresh data')
                result = func(*args, **kwargs)

                # Cache it
                if result is not None:
                    cache[cache_key] = (now, result)

                return result
            
            # Add cache management methods
            wrapper.clear_cache = lambda: cache.clear()
            wrapper.get_cache_info = lambda: {
                 "size": len(cache),
                "keys": list(cache.keys())
            }
            
            return wrapper
        return decorator
    
    @staticmethod
    def retry_on_failure(max_attempts=3, delay=1, backoff=2):
        """Retry failed operations with exponential backoff"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                current_delay = delay
                
                for attempt in range(1, max_attempts + 1):
                    try:
                        result = func(*args, **kwargs)
                        
                        if result is not None:
                            if attempt > 1:
                                print(f"✓ Succeeded on attempt {attempt}/{max_attempts}")
                            return result
                        
                        # None result, but no exception - might be valid
                        if attempt == max_attempts:
                            return result
                            
                    except Exception as e:
                        if attempt < max_attempts:
                            print(f"🔄 Attempt {attempt}/{max_attempts} failed: {e}")
                            print(f"   Retrying in {current_delay}s...")
                            time.sleep(current_delay)
                            current_delay *= backoff  # Exponential backoff
                        else:
                            print(f"❌ All {max_attempts} attempts failed: {e}")
                            return None
                
                return None
            return wrapper
        return decorator
    
    @staticmethod
    def validate_input(**type_checks):
        """Validate function inputs with type checking"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                errors = []
                
                # Validate kwargs
                for param, expected_type in type_checks.items():
                    if param in kwargs:
                        value = kwargs[param]
                        if not isinstance(value, expected_type):
                            errors.append(
                                f"{param}: expected {expected_type.__name__}, "
                                f"got {type(value).__name__}"
                            )
                
                if errors:
                    error_msg = "Validation errors: " + "; ".join(errors)
                    print(f"❌ {error_msg}")
                    raise ValueError(error_msg)
                
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    @staticmethod
    def rate_limit(max_calls=10, time_window=60):
        """Rate limit function calls"""
        calls = []
        
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                now = time.time()
                
                # Remove old calls outside time window
                nonlocal calls
                calls = [call_time for call_time in calls if now - call_time < time_window]
                
                # Check if rate limit exceeded
                if len(calls) >= max_calls:
                    wait_time = time_window - (now - calls[0])
                    print(f"⏸️  Rate limit reached. Try again in {wait_time:.1f}s")
                    return None
                
                # Record this call
                calls.append(now)
                
                return func(*args, **kwargs)
            return wrapper
        return decorator


def get_activity_log(limit=50):
    """Retrieve recent activity log entries"""
    AppDecorators.ensure_log_dir()
    
    try:
        with open(AppDecorators.ACTIVITY_LOG, 'r') as f:
            logs = [json.loads(line) for line in f.readlines()]
        return logs[-limit:]  # Return last N entries
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error reading log: {e}")
        return []


def get_performance_stats():
    """Get performance statistics"""
    AppDecorators.ensure_log_dir()
    
    try:
        with open(AppDecorators.PERFORMANCE_LOG, 'r') as f:
            logs = [json.loads(line) for line in f.readlines()]
        
        if not logs:
            return {"message": "No performance data yet"}
        
        # Calculate stats
        by_function = {}
        for log in logs:
            func = log['function']
            duration = log['duration_ms']
            
            if func not in by_function:
                by_function[func] = []
            by_function[func].append(duration)
        
        # Aggregate
        stats = {}
        for func, durations in by_function.items():
            stats[func] = {
                "calls": len(durations),
                "avg_ms": round(sum(durations) / len(durations), 2),
                "min_ms": round(min(durations), 2),
                "max_ms": round(max(durations), 2)
            }
        
        return stats
        
    except FileNotFoundError:
        return {"message": "No performance data yet"}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    # Test decorators
    print("Testing Enhanced Decorators...\n")
    
    @AppDecorators.timer
    @AppDecorators.audit_log("TEST", include_result=True)
    @AppDecorators.cache_with_ttl(ttl_minutes=1)
    def slow_function(x):
        time.sleep(0.5)
        return x * 2
    
    print("Call 1 (should be slow):")
    result1 = slow_function(5)
    print(f"Result: {result1}\n")
    
    print("Call 2 (should be cached):")
    result2 = slow_function(5)
    print(f"Result: {result2}\n")
    
    print("✓ Decorators working!\n")
    
    # Show logs
    print("Activity Log:")
    for log in get_activity_log(limit=5):
        print(f"  {log}")
    
    print("\nPerformance Stats:")
    print(get_performance_stats())