"""
Calculator 2.0 - Main Entry Point
Modular calculator system with OOP architecture

usage: python main.py
"""

from calculator_menu import calculator_menu


def main():
    """Entry point for calculator 2.0"""
    print('='*60)
    print('Starting Calculator 2.0 ...')
    print('Modular Architecture - Day 11 Project')
    print('='*60)

    calculator_menu()

    if __name__ == '__main__':
        main()
        
