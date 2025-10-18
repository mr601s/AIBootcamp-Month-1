"""
RPG Character System - Day 9: Inheritance & Polymorphism
A role-playing game character management system demonstrating OOP principles
"""

class Character:
    """Base character class - parent of all character types"""

    def __init__(self, name, health=100):
        """Initialize a character
        
        Args:
            name (str): character's name
            health (int): Starting health points (default 100)
    """
        self.name = name
        self.health = health
        self.max_health = health
        self.level = 1
        self.experience = 0
        self.inventory = []
        print(f' {name} has been created!')

    def attack(self):
        """Basic attack - returns damage amount
        
        Returns:
            int: Damage dealt
        """
        damage = 10
        print(f' {self.name} attacks for {damage} damage!')
        return damage
    
    def take_damage(self, damage):
        """Take damage and reduce health
        
        Args:
            damage (int): Amount of damage to take
        """
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f' {self.name} takes {damage} damage! Health is now {self.health}/{self.max_health}.')

    def is_alive(self):
        """Check if character is still alive

        Returns:
            bool: True if health > 0, False otherwise
        """
        return self.health > 0
    
    def heal(self, amount):
        """Restore health
        
        Args:
            amount (int): Amount of health to restore
        """
        old_health = self.health
        self.health += amount

        # Can't exceed max health
        if self.health > self.max_health:
            self.health = self.max_health

        actual_heal = self.health - old_health
        print(f' {self.name} heals for {actual_heal} points! Health is now {self.health}/{self.max_health}.')

    def add_item(self,item):
        """Add item to inventory
        
        Args:
            item (str): Item to add
        """
        self.inventory.append(item)
        print(f' {self.name} acquired: {item}')

    def show_inventory(self):
        """Display character's inventory"""
        print(f'\n {self.name}\'s Inventory:')
        if not self.inventory:
            print(' Empty')
        else:
            for i, item in enumerate(self.inventory, 1):
                print(f' {i}. {item}')

    def gain_experience(self, exp):
        """Gain experience points
        
        Args:
            exp (int): Experience points to gain
        """
        self.experience += exp
        print(f' {self.name} gains {exp} experience points! Total EXP: {self.experience}')

        # Check for level up (every 100 XP)
        if self.experience >= self.level * 100:
            self.level_up()

    def level_up(self):
        """Level up the character"""
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        print(f' {self.name} leveled up to Level {self.level}! Max Health is now {self.max_health}.')

    def display_stats(self):
        """Display character stats"""
        print(f'\n{"="*50}')
        print(f' Character Stats')
        print(f' Name: {self.name}')
        print(f' Level: {self.level}')
        print(f' Health: {self.health}/{self.max_health}')
        print(f' Experience: {self.experience}')
        print(f' Inventory: {", ".join(self.inventory) if self.inventory else "Empty"}')
        print(f'{"="*50}\n')
                 
class Mage(Character):
    """Mage class - Uses mana to cast powerful spells"""

    def __init__(self, name):
        """Initialize a Mage
        
        Args:
            name (str): Mage's name
        """

        # Call parent's __init__ with LOWER health (mages are fragile!)
        super().__init__(name, health=80)

        # Mage specific attributes
        self.mana = 100
        self.max_mana = 100
        self.spells = ['Fireball', 'Ice Shard', 'Lightning Bolt']

        print(f'✨ {name} is a powerful Mage with {self.mana} mana!')

    def attack(self):
        """Mage attack - uses mana to cast spells
        
        Returns:
            int: Damage dealt
        """
        mana_cost = 15

        if self.mana >= mana_cost:
            self.mana -= mana_cost
            damage = 30
            print(f'🔥 {self.name} casts Fireball for {damage} damage! Mana left: {self.mana}/{self.max_mana}')
            return damage
        else:
            # Out of mana! Weak physical attack
            damage = 5
            print(f'💨 {self.name} is out of mana and attacks weakly for {damage} damage!')
            return damage
        
    def special_attack(self):
        """Special ability - Meteor Storm (Costs 50 mana)
        
        Returns:
            int: Damage dealt (0 if not enough mana)
        """
        mana_cost = 50

        if self.mana >= mana_cost:
            self.mana -= mana_cost
            damage = 70
            print(f'🌩️ {self.name} unleashes Meteor Storm for {damage} damage! Mana left: {self.mana}/{self.max_mana}')
            return damage
        else:
            print(f'❌ {self.name} does not have enough mana for Meteor Storm!')
            return 0
        
    def restore_mana(self, amount):
        """Restore mana
        
        Args:
            amount (int): AMount of mana to restore
        """
        old_mana = self.mana
        self.mana += amount

        # Can't exceed max mana
        if self.mana > self.max_mana:
            self.mana = self.max_mana

        actual_restore = self.mana - old_mana
        print(f'🔮 {self.name} restores {actual_restore} mana points! Mana is now {self.mana}/{self.max_mana}.')

    def meditate(self):
        """Meditate to restore mana (restores 30 mana)"""
        print(f'🧘 {self.name} meditates to restore mana.')
        self.restore_mana(30)

    def cast_spell(self, spell_name):
        """Cast a specific spell
        
        Args:
            spell_name (str): Name of spell to cast
        """

        if spell_name not in self.spells:
            print(f'❌ {self.name} does not know the spell: {spell_name}!')
            return 0
        
        mana_cost = {
            'Fireball': 30,
            'Ice Shard': 20,
            'Lightning Bolt': 25
        }

        damages = {
            'Fireball': 40,
            'Ice Shard': 25,
            'Lightning Bolt': 35
        }

        cost = mana_cost[spell_name]

        if self.mana >= cost:
            self.mana -= cost
            damage = damages[spell_name]

            spell_emojis = {
                'Fireball': '🔥',
                'Ice Shard': '❄️',
                'Lightning Bolt': '⚡'
            }

            emoji = spell_emojis[spell_name]
            print(f'{emoji} {self.name} casts {spell_name} for {damage} damage! Mana left: {self.mana}/{self.max_mana}')
            return damage
        else:
            print(f'❌ {self.name} does not have enough mana to cast {spell_name}!')
            return 0
        
    def learn_spell(self, spell_name):
        """Learn a new spell
        
        Args:
            spell_name (str): Name of spell to learn
        """
        if spell_name not in self.spells:
            self.spells.append(spell_name)
            print(f'✨ {self.name} has learned a new spell: {spell_name}!')
        else:
            print(f'ℹ️ {self.name} already knows the spell: {spell_name}.')

    def show_spells(self):
        """Display known spells"""
        print(f'\n{self.name}\'s Spellbook:')
        if not self.spells:
            print(' No spells known.')
        else:
            for i, spell in enumerate(self.spells, 1):
                print(f' {i}. {spell}')

    def display_stats(self):
        """Display mage stats - overrides parent to show mana and spells"""
        # Call parent's display_stats first
        super().display_stats()

        # Add mage-specific stats
        print(f' Mana: {self.mana}/{self.max_mana}')
        print(f' Known Spells: {", ".join(self.spells) if self.spells else "None"}')
        print(f'{"="*50}\n')

class Archer(Character):
    """ Archer class - Ranged attacks, critical, arrow management"""

    def __init__(self, name):
        """Initialize an Archer
        
        Args:
            name (str): Archer's name
        """

        # Call parent's __init__ with normal health
        super().__init__(name, health=100)

        # Archer-specific attributes
        self.arrows = 30
        self.max_arrows = 30
        self.accuracy = 85 # 85% hit chance
        self.crit_chance = 25 # 25% critical hit chance 

        print(f'🏹 {name} is a skilled Archer with {self.arrows} arrows!')

    def attack(self):
        """Archer attack - ranged with chance to miss or crit
        
        Returns:
            int: Damage dealt (0 if miss)
        """
        if self.arrows <= 0:
            damage = 5
            print(f'❌ {self.name} is out of arrows and attacks weakly for {damage} damage!')
            return damage 
        
        # Use an arrow
        self.arrows -= 1

        # Check if hit lands
        import random
        hit_roll = random.randint(1, 100)

        if hit_roll > self.accuracy:
            print(f'💨 {self.name}\'s arrow missed!')
            return 0
        
        # Hit landed! Check for critical
        crit_roll = random.randint(1, 100)

        if crit_roll <= self.crit_chance:
            # Critical Hit!
            damage = 45
            print(f'💥 {self.name} lands a CRITICAL HIT for {damage} damage! Arrows left: {self.arrows}/{self.max_arrows}')
            return damage
        else:
            # Normal hit
            damage = 22
            print(f'🏹 {self.name} shoots an arrow for {damage} damage! Arrows left: {self.arrows}/{self.max_arrows}')
            return damage
        
    def special_attack(self):
        """Special ability - Rain of Arrows (shoots 5 arrows at once)
        
        Returns:
            int: Total damage dealt
        """
        arrows_needed = 5

        if self.arrows < arrows_needed:
            print(f'❌ {self.name} does not have enough arrows for Rain of Arrows!')
            return 0
        
        total_damage = 0
        print(f'🌧️ {self.name} unleashes Rain of Arrows!')

        for _ in range(arrows_needed):
            damage = self.attack()
            total_damage += damage

        return total_damage
    
    def reload_arrows(self, amount):
        """Reload arrows
        
        Args:
            amount (int): Number of arrows to reload
        """
        old_arrows = self.arrows
        self.arrows += amount

        # Can't exceed max arrows
        if self.arrows > self.max_arrows:
            self.arrows = self.max_arrows

        actual_reload = self.arrows - old_arrows
        print(f'🔄 {self.name} reloads {actual_reload} arrows! Arrows are now {self.arrows}/{self.max_arrows}.')

    def aimed_shot(self):
        """Aimed Shot - guaranteed hit with increased damage (costs 2 arrows)
        
        Returns:
            int: Damage dealt (0 if not enough arrows)
        """
        arrows_needed = 2

        if self.arrows < arrows_needed:
            print(f'❌ {self.name} does not have enough arrows for Aimed Shot!')
            return 0
        
        # Use 2 arrows
        self.arrows -= arrows_needed
        damage = 40
        print(f'🎯 {self.name} performs Aimed Shot for {damage} damage! Arrows left: {self.arrows}/{self.max_arrows}')
        return damage
    
    def display_stats(self):
        """Display archer stats - overrides parent to show arrows and accuracy"""
        # Call parent's display_stats first
        super().display_stats()

        # Add archer-specific stats
        print(f' Arrows: {self.arrows}/{self.max_arrows}')
        print(f' Accuracy: {self.accuracy}%')
        print(f' Critical Hit Chance: {self.crit_chance}%')
        print(f'{"="*50}\n')

class Warrior(Character):
    """Warrior class - High health, heavy armor, powerful melee attacks"""

    def __init__(self, name):
        """Initialize a Warrior
        
        Args:
            name (str): Warrior's name
        """
        # Call parent's __init__ with HIGHER health (warriors are tough!)
        super().__init__(name, health=150)

        # Warrior-specific attributes
        self.armor = 20
        self.rage = 0
        self.max_rage = 100

        print(f'⚔️ {name} is a mighty Warrior with {self.armor} armor!')

    def attack(self):
        """Warrior attack - strong melee damage
        
        Returns:
            int: Damage dealt
        """
        damage = 25
        print(f'⚔️ {self.name} swings their sword for {damage} damage!')
        
        # Gain rage from attacking
        self.rage = min(self.rage + 10, self.max_rage)
        
        return damage

    def special_attack(self):
        """Special ability - Berserker Rage (requires 50 rage)
        
        Returns:
            int: Damage dealt (0 if not enough rage)
        """
        rage_cost = 50

        if self.rage >= rage_cost:
            self.rage -= rage_cost
            damage = 60
            print(f'💢 {self.name} unleashes Berserker Rage for {damage} damage! Rage left: {self.rage}/{self.max_rage}')
            return damage
        else:
            print(f'❌ {self.name} does not have enough rage for Berserker Rage!')
            return 0

    def display_stats(self):
        """Display warrior stats - overrides parent to show armor and rage"""
        # Call parent's display_stats first
        super().display_stats()

        # Add warrior-specific stats
        print(f' Armor: {self.armor}')
        print(f' Rage: {self.rage}/{self.max_rage}')
        print(f'{"="*50}\n')

def battle(character1, character2):
    """Simulate a battle between two characters
    
    Args:
        character1 (Character): First fighter
        Character2 (Character): Second fighter
    """
    print(f'\n{"="*60}')
    print(f'⚔️ Battle Start: {character1.name} vs {character2.name} ⚔️')
    print(f'{"="*60}\n')

    round_num = 1

    while character1.is_alive() and character2.is_alive():
        print(f'\n--- Round {round_num} ---\n')
        print(f'{character1.name}: {character1.health}/{character1.max_health} HP')
        print(f'{character2.name}: {character2.health}/{character2.max_health} HP')
        print()

        # Character 1 attacks
        print(f'>>> {character1.name}\'s turn:')
        damage = character1.attack()
        if damage > 0:
            character2.take_damage(damage)

        # Check if character 2 is defeated
        if not character2.is_alive():
            print(f'\n{"="*60}')
            print(f'🏆 {character1.name} wins the battle! 🏆')
            print(f'{"="*60}')
            break

        print()

        # Character 2 attacks
        print(f'>>> {character2.name}\'s turn:')
        damage = character2.attack()
        if damage > 0:
            character1.take_damage(damage)

        # Check if character 1 is defeated
        if not character1.is_alive():
            print(f'\n{"="*60}')
            print(f'🏆 {character2.name} wins the battle! 🏆')
            print(f'{"="*60}')
            break

        round_num += 1

        # Safety limit (prevent infinite battles)
        if round_num > 50:
            print(f'\n{"="*60}')
            print('⚖️ The battle ends in a draw due to time limit! ⚖️')
            print(f'{"="*60}')
            break

    print(f'\nFinal Status:')
    print(f' {character1.name}: {character1.health}/{character1.max_health} HP')
    print(f' {character2.name}: {character2.health}/{character2.max_health} HP\n')

# COMPLETE RPG SYSTEM TEST
if __name__ == "__main__":
    print("="*70)
    print("🎮 COMPLETE RPG CHARACTER SYSTEM - DAY 9 FINALE")
    print("="*70)
    
    # Create all character types
    print("\n" + "="*70)
    print("CHARACTER CREATION")
    print("="*70)
    
    hero = Character("Hero")
    warrior = Warrior("Conan")
    mage = Mage("Gandalf")
    archer = Archer("Legolas")
    
    all_characters = [hero, warrior, mage, archer]
    
    # Display all stats
    print("\n" + "="*70)
    print("ALL CHARACTER STATS")
    print("="*70)
    
    for char in all_characters:
        char.display_stats()
    
    # Test polymorphism - same method, different behavior
    print("\n" + "="*70)
    print("POLYMORPHISM DEMO - ALL CHARACTERS ATTACK!")
    print("="*70)
    
    for char in all_characters:
        print(f"\n{char.name} ({char.__class__.__name__}):")
        char.attack()
        char.attack()  # Attack twice to show mechanics
    
    # Test archer features
    print("\n" + "="*70)
    print("ARCHER SPECIAL FEATURES TEST")
    print("="*70)
    
    print("\n--- Testing Multi-Shot ---")
    archer.special_attack()
    
    print("\n--- Testing Aimed Shot ---")
    archer.aimed_shot()
    
    print("\n--- Testing Arrow Reload ---")
    archer.reload_arrows(10)
    
    # Battle 1: Warrior vs Mage
    print("\n" + "="*70)
    print("BATTLE 1: WARRIOR VS MAGE")
    print("="*70)
    
    battle_warrior = Warrior("Thorin")
    battle_mage = Mage("Saruman")
    
    battle(battle_warrior, battle_mage)
    
    # Battle 2: Archer vs Warrior
    print("\n" + "="*70)
    print("BATTLE 2: ARCHER VS WARRIOR")
    print("="*70)
    
    battle_archer = Archer("Robin Hood")
    battle_warrior2 = Warrior("Knight")
    
    battle(battle_archer, battle_warrior2)
    
    # Battle 3: Mage vs Archer
    print("\n" + "="*70)
    print("BATTLE 3: MAGE VS ARCHER")
    print("="*70)
    
    battle_mage2 = Mage("Merlin")
    battle_archer2 = Archer("Artemis")
    
    battle(battle_mage2, battle_archer2)
    
    # Final summary
    print("\n" + "="*70)
    print("🎉 DAY 9 COMPLETE - RPG CHARACTER SYSTEM")
    print("="*70)
    print("\n✅ Features Implemented:")
    print("   • Base Character class with health, inventory, leveling")
    print("   • Warrior class with armor and rage attacks")
    print("   • Mage class with mana and spell system")
    print("   • Archer class with arrows and critical hits")
    print("   • Complete battle system with turn-based combat")
    print("   • Inheritance and polymorphism demonstrated")
    print("   • Method overriding and code reuse")
    print("\n💪 OOP Concepts Mastered:")
    print("   • Classes and objects")
    print("   • Inheritance")
    print("   • Polymorphism")
    print("   • Method overriding")
    print("   • super() function")
    print("   • Code reuse and DRY principle")
    print("\n🎮 Total Classes: 4")
    print("   Total Lines: ~600+")
    print("   Total Features: 20+")
    print("\n" + "="*70)                        