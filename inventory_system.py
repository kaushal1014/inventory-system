"""
Inventory Management System

A simple inventory management system for tracking stock quantities,
adding/removing items, and generating reports.
"""
import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add items to inventory with optional logging.

    Args:
        item (str): Name of the item to add
        qty (int): Quantity to add
        logs (list): Optional list to log operations
    """
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{str(datetime.now())}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove items from inventory.

    Args:
        item (str): Name of the item to remove
        qty (int): Quantity to remove
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Warning: Item '{item}' not found in inventory")
    except (TypeError, ValueError):
        print(f"Warning: Invalid quantity type for item '{item}'")


def get_qty(item):
    """Get quantity of an item in inventory.

    Args:
        item (str): Name of the item

    Returns:
        int: Quantity of the item
    """
    return stock_data[item]


def load_data(file="inventory.json"):
    """Load inventory data from JSON file.

    Args:
        file (str): Path to the JSON file

    Returns:
        dict: The loaded inventory data
    """
    global stock_data  # pylint: disable=global-statement
    with open(file, "r", encoding="utf-8") as f:
        stock_data = json.loads(f.read())
    return stock_data


def save_data(file="inventory.json"):
    """Save inventory data to JSON file.

    Args:
        file (str): Path to the JSON file
    """
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data))


def print_data():
    """Print current inventory report."""
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])


def check_low_items(threshold=5):
    """Check for items with low stock levels.

    Args:
        threshold (int): Minimum stock level threshold

    Returns:
        list: List of items below threshold
    """
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """Main function to demonstrate inventory system functionality."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    # Removed eval() for security - replaced with direct print
    print('Direct print instead of eval')


main()
