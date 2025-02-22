# Library Database Project

This project is dedicated to designing and implementing a comprehensive database for a library. The objective is to create a system that efficiently manages library resources, events, personnel, and future acquisitions.

## Overview

The Library Database Project covers the following key areas:

- **Resource Management:**  
  The database includes various items such as print books, online books, magazines, scientific journals, CDs, records, and more.

- **Circulation System:**  
  Users can borrow items with a due date, and the system tracks returns and fines for overdue items.

- **Event Management:**  
  The library hosts a range of events—from book clubs and art shows to film screenings—targeted at specific audiences. These events are held in dedicated social rooms and are free to attend.

- **Personnel & Record Keeping:**  
  Detailed records are maintained for library staff as well as items that might be added in the future.

## Project Phases

### 1. Domain Definition
- **Purpose:** Define the project scope and detail the requirements for a library database.
- **Tasks:**  
  - Identify all types of items available in the library.
  - Outline the borrowing, returning, and fine systems.
  - Describe library events and target audiences.
  - Document personnel and future acquisition records.
  
### 2. Entity-Relationship Diagrams (ERDs)
- **Purpose:** Develop a clear visual representation of the database structure.
- **Tasks:**  
  - Create ER diagrams using standard notations.
  - Define entities, attributes, and relationships with appropriate key and participation constraints.
  - Ensure a diverse use of entities to represent the real-world complexities of a library system.

### 3. Anomaly and Dependency Analysis
- **Purpose:** Ensure the database design is robust and free from anomalies.
- **Tasks:**  
  - Analyze all non-trivial functional dependencies.
  - Verify that the design is free of bad dependencies.
  - Decompose relations as needed to achieve Boyce-Codd Normal Form (BCNF).
  - Provide detailed documentation explaining why the final design avoids anomalies.

### 4. SQL Schema Development
- **Purpose:** Translate the ER diagrams into a working database schema using SQLite.
- **Tasks:**  
  - Create tables, define required constraints, and implement triggers to ensure data integrity.
  - Prepare the schema for realistic library operations.

### 5. Data Population
- **Purpose:** Populate the database with realistic data.
- **Tasks:**  
  - Insert at least 10 realistic tuples into each table.
  - Use data generators or real data sources to simulate an operational library database.

### 6. Database Application Development
- **Purpose:** Build an application that interacts with the database.
- **Tasks:**  
  - Develop a Python application using SQLite.
  - Implement features that allow users to:
    - **Search for items:** Easily find resources within the library.
    - **Borrow items:** Manage the checkout process.
    - **Return items:** Track returns and manage due dates.
    - **Donate items:** Accept contributions to the library.
    - **Find and register for events:** Discover and sign up for library events.
    - **Volunteer:** Allow users to volunteer at the library.
    - **Request assistance:** Enable users to ask for help from a librarian.

