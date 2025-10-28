"""
File Organizer 3000
Organizes files by tape into categorized folders
"""

from pathlib import Path
from datetime import datetime
import shutil
import json

class FileOrganizer:
    """Organizes files in a directory by type"""

    # File type categories
    CATEGORIES = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
        'Spreadsheets': ['.xls', '.xlsx', '.csv', '.ods'],  # CSV is here
        'Presentations': ['.ppt', '.pptx', '.odp'],  # PPTX is here
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
        'Video': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
        'Other': []
    }
    def __init__(self, source_dir):
        """Initialize organizer with source directory"""
        self.source_dir = Path(source_dir)
        self.log = []
        self.stats = {
            'total_files': 0,
            'organized': 0,
            'skipped': 0,
            'errors': 0,
            'categories': {}
        }

        # Initialize category stats 
        for category in self.CATEGORIES.keys():
            self.stats['categories'][category] = 0

    def get_category(self, file_path):
        """Determine category for a file based on extension"""
        extension = file_path.suffix.lower()

        for category, extensions in self.CATEGORIES.items():
            if extension in extensions:
                return category
            
        return 'Other'
    
    def _should_skip(self, file_path):
        """Check if file should be skipped"""
        skip_files = {
            'file_organizer.py',
            'organization_log.json', 
            'organization_report.txt'
        }
        return file_path.name in skip_files
    
    def organize(self, dry_run=False):
        """
        Organize files in the source directory
        
        Args:
            dry_run: If True, only simulate (don't actually move files)
        """
        print(f"\n{'='*60}")
        print(f"FILE ORGANIZER 3000")
        print(f"{'='*60}")
        print(f"Source Directory: {self.source_dir}")
        print(f"Mode: {'DRY RUN (Simulation)' if dry_run else 'LIVE (Moving Files)'}")
        print(f"{'='*60}\n")
        
        # Check if source directory exists
        if not self.source_dir.exists():
            print(f"❌ Error: Directory '{self.source_dir}' does not exist!")
            return
        
        # Get all files in source directory (not subdirectories)
        files = [f for f in self.source_dir.iterdir() if f.is_file()]
        self.stats['total_files'] = len(files)
        
        if len(files) == 0:
            print("📁 No files found to organize.")
            return
        
        print(f"📊 Found {len(files)} files to organize\n")
        
        # Process each file
        for file_path in files:
            try:
                # Skip files we should ignore
                if self._should_skip(file_path):
                    self._log_action('SKIP', file_path, f'Skipping system/organizer file')
                    self.stats['skipped'] += 1
                    print(f"⏭️  Skipping: {file_path.name}")
                    continue

                # Determine category
                category = self.get_category(file_path)

                # Create category folder if needed
                category_folder = self.source_dir / category

                if not dry_run:
                    category_folder.mkdir(exist_ok=True)

                # Determined new path
                new_path = category_folder / file_path.name

                # Handle duplicate names
                if new_path.exists() and not dry_run:
                    # Add timestamp to make unique 
                    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                    new_name = f'{file_path.stem}_{timestamp}{file_path.suffix}'
                    new_path = category_folder / new_name

                # Move the file (or simulate)
                if not dry_run:
                    shutil.move(str(file_path), str(new_path))

                # Log the action
                self._log_action('MOVE', file_path, f'{category}/{new_path.name}')
                self.stats['organized'] += 1
                self.stats['categories'][category] += 1

                print(f'✅ {file_path.name} -> {category}/')

            except Exception as e:
                self._log_action('ERROR', file_path, str(e))
                self.stats['errors'] += 1
                print(f'❌ Error organizing {file_path.name}: {e}')

        # Print summary
        self._print_summary()

        # Save log and report (only if not dry run)
        if not dry_run:
            self._save_log()
            self._save_report()

    def _log_action(self, action, file_path, details):
        """Add entry to log"""
        entry = {
            'timestamp': datetime.now().isoformat(),
            'action': action,
            'file': file_path.name,
            'details': details
        }
        self.log.append(entry)
        
    def _print_summary(self):
        """Print organization summary"""
        print(f'\n{'='*60}')
        print('ORGANIZATION SUMMARY')
        print(f"{'='*60}")
        print(f"Total Files: {self.stats['total_files']}")
        print(f"Organized: {self.stats['organized']}")
        print(f"Skipped: {self.stats['skipped']}")
        print(f"Errors: {self.stats['errors']}")
        print(f"\nFiles by Category:")

        for category, count in self.stats['categories'].items():
            if count > 0:
                print(f' {category}: {count}')

        print(f"{'='*60}")

    def _save_log(self):
        """Save detailed log to JSON file"""
        log_file = self.source_dir / 'organization_log.json'

        with open(log_file, 'w') as f:
            json.dump(self.log, f, indent=2)

        print(f'Detailed log saved to: {log_file}')

    def _save_report(self):
        """Save human-readable report"""
        report_file = self.source_dir / 'organization_report.txt'

        with open(report_file, 'w') as f:
            f.write('FILE ORGANIZATION REPORT\n')
            f.write('=' * 60 + '\n\n')
            f.write(f'Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n')
            f.write(f'Directory: {self.source_dir}\n\n')

            f.write('SUMMARY\n')
            f.write("-" * 60 + "\n")
            f.write(f"Total Files: {self.stats['total_files']}\n")
            f.write(f"Organized: {self.stats['organized']}\n")
            f.write(f"Skipped: {self.stats['skipped']}\n")
            f.write(f"Errors: {self.stats['errors']}\n\n")

            f.write("FILES BY CATEGORY\n")
            f.write("-" * 60 + "\n")
            for category, count in self.stats['categories'].items():
                if count > 0:
                    f.write(f"{category}: {count}\n")
        
            f.write("\n" + "=" * 60 + "\n")
            f.write("DETAILED LOG\n")
            f.write("=" * 60 + "\n\n")
        
            for entry in self.log:
                f.write(f"[{entry['timestamp']}] {entry['action']}: {entry['file']}\n")
                f.write(f"  → {entry['details']}\n\n")
    
        print(f"📄 Report saved to: {report_file}")


def main():
    """Main function"""
    print('\nFILE ORGANIZER 3000')
    print('Organize your messy directories!\n')

    # Get directory from user
    directory = input('Enter directory path to organize (or "." for current): ').strip()

    if not directory:
        directory = '.'

    # Ask for dry run
    dry_run_input = input('\nDry run first? (y/n): ').strip().lower()
    dry_run = dry_run_input == 'y'

    # Create organizer and run
    organizer = FileOrganizer(directory)
    organizer.organize(dry_run=dry_run)

    # If was dry run, ask if they want to do it for real
    if dry_run:
        proceed = input('\nProceed with actual organization? (y/n): ').strip().lower()
        if proceed == 'y':
            organizer = FileOrganizer(directory)
            organizer.organize(dry_run=False)


if __name__ == '__main__':
    main()