# 🚲 Eco-Ride Urban Mobility & Fleet Management System

## 📌 Project Overview

**Eco-Ride** is a **console-based Urban Mobility & Fleet Management System** developed using **Python Object-Oriented Programming (OOP)** principles.
The system manages **Electric Cars and Electric Scooters** across **multiple fleet hubs**, supports **searching, sorting, analytics**, ensures **data persistence using CSV & JSON**, and includes **automated testing with Pytest**.

This project demonstrates **real-world application design**, **clean architecture**, **incremental feature development**, and **testing best practices** using **Git branch-based workflows**.

---

## 🎯 Key Objectives

* Apply **OOP pillars**: Encapsulation, Inheritance, Abstraction, Polymorphism
* Manage fleet data using **collections and dictionaries**
* Ensure **data integrity** and prevent duplicates
* Implement **search, sorting, and analytics** features
* Persist data using **CSV & JSON File I/O**
* Build a **menu-driven console application**
* Add **automated unit testing using Pytest**
* Perform **data analytics & transformation scripts**

---

## 🏗️ Project Architecture

```text
eco-ride-urban-mobility-system/
│
├── Vehicle.py                  # Abstract base class
├── ElectricCar.py              # Electric Car logic
├── ElectricScooter.py          # Electric Scooter logic
├── FleetManager.py             # Fleet & hub management
├── EcoRideMain.py              # Menu-driven application
│
├── fleet_data.csv              # CSV persistence
├── fleet_data.json             # JSON persistence
│
├── battery_filter_script.py    # Battery analytics script (UC15)
│
├── tests/
│   ├── test_vehicle.py
│   ├── test_fleet_manager.py
│   └── test_operations.py      # Pytest cases (UC16)
│
├── requirements.txt
└── README.md
```

---

## 🧠 Core Design Philosophy

The project follows **separation of concerns**:

* **Vehicle Hierarchy** → Vehicle rules & validation
* **FleetManager** → Business logic & operations
* **Main Program** → User interaction
* **Scripts** → Analytics & transformation
* **Tests** → Automated verification

This improves **scalability, maintainability, and testability**.

---

## 🚘 Vehicle Hierarchy

### 🔹 Vehicle (Abstract Base Class)

* Uses `abc.ABC`
* Common attributes:

  * `vehicle_id`
  * `model`
  * `battery_percentage`
  * `maintenance_status`
  * `rental_price`
* Implements:

  * **Encapsulation** with private variables
  * **Validation** using setters
  * `__eq__` to prevent duplicate IDs
  * `__str__` for clean output
* Declares abstract method:

  ```python
  calculate_trip_cost()
  ```

---

### 🚗 ElectricCar

* Inherits from `Vehicle`
* Adds `seating_capacity`
* Overrides `calculate_trip_cost(distance)`
* Fare:

  ```
  Base fare + cost per kilometer
  ```

---

### 🛴 ElectricScooter

* Inherits from `Vehicle`
* Adds `max_speed_limit`
* Overrides `calculate_trip_cost(time)`
* Fare:

  ```
  Base fare + cost per minute
  ```

---

## 🗂️ Fleet Management (FleetManager)

### 🔹 UC6 – Multiple Fleet Hubs

* Dictionary-based hub management:

  ```python
  { hub_name: [vehicle_objects] }
  ```

---

### 🔹 UC7 – Data Integrity

* Prevents duplicate vehicle IDs within a hub
* Uses:

  * `__eq__`
  * List comprehension

---

### 🔹 UC8 – Search Functionality

* Search by:

  * Hub
  * Battery percentage (>80%)
* Uses:

  * `filter()`
  * `lambda`

---

### 🔹 UC9 – Categorized View

* Groups vehicles by type (Car / Scooter)
* Uses:

  * `isinstance()`
  * Dictionary mapping

---

### 🔹 UC10 – Fleet Analytics

* Counts vehicles by status:

  * Available
  * On Trip
  * Under Maintenance
* Uses dictionary counters

---

### 🔹 UC11 – Alphabetical Sorting

* Sorts vehicles by model name
* Uses:

  ```python
  sort(key=lambda v: v.model)
  ```

---

### 🔹 UC12 – Advanced Sorting

* Sorts by:

  * Battery (descending)
  * Fare price (descending)
* Uses:

  ```python
  sorted(..., reverse=True)
  ```

---

## 💾 UC13 – CSV Persistence

### Save to CSV

* Stores complete fleet data
* One row per vehicle

### Load from CSV

* Recreates:

  * Vehicle objects
  * Hub structure
* Clears in-memory data before loading

---

## 🔄 UC14 – JSON Persistence

* Saves full fleet structure into JSON
* Supports nested hub → vehicle mapping
* Enables object serialization & deserialization
* Useful for APIs and future integrations

---

## 📊 UC15 – Battery Range Analytics Script

* Separate analytics script
* Reads `fleet_data.csv`
* Categorizes vehicles into battery ranges:

  * 0–60
  * 60–70
  * 70–100
* Exports structured JSON:

  ```json
  {
    "battery_0_60": [...],
    "battery_60_70": [...],
    "battery_70_100": [...]
  }
  ```
* Demonstrates **data transformation & analytics**

---

## 🧪 UC16 – Automated Testing with Pytest

* Unit tests for:

  * Battery validation
  * Rental price validation
  * Fare calculation (polymorphism)
  * Hub creation
  * Duplicate vehicle prevention
* Uses:

  * `pytest`
  * `@pytest.mark`
* Business logic tested separately from UI

Example:

```bash
pytest -v
pytest -m tripcost
```

---

## 📋 Menu-Driven Application

Users can:

1. Add hubs & vehicles
2. Search vehicles
3. View by type
4. Fleet analytics
5. Sort vehicles
6. Save/load CSV
7. Save/load JSON
8. Exit

---

## 🛠️ Technologies Used

* Python 3
* OOP (Encapsulation, Inheritance, Abstraction, Polymorphism)
* CSV & JSON File I/O
* Pytest
* Git & GitHub

---

## 🧾 Git Workflow

* Each Use Case → separate Git branch
* Merged into `main` after completion
* Commit format:

  ```
  UC<number>: Description
  ```

---

## ✅ Current Status

✔ UC1 – UC16 completed
✔ CSV & JSON persistence working
✔ Battery analytics script added
✔ Pytest automation implemented
✔ Project is **reviewer & interview ready**

---

## 📌 Conclusion

Eco-Ride is a **complete, end-to-end fleet management system** showcasing Python OOP, file handling, analytics, and automated testing.
The project is designed to be **extensible**, **maintainable**, and aligned with **real-world backend development practices**.
