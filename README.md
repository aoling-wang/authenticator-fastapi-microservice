FastAPI Authenticator Microservice

Hook Me Up, Scotty! A versatile authenticator microservice that requires minimal adjustments to implement into small to mid-sized applications.

**

Visual Demo

**

Built on FastAPI, this light-weight authenticator was made with modularity and flexibility in mind. With how fast the modern user landscape and cybersecurity practices evolved, a key concern is how microservices can be updated and connected to applications without interrupting user experience or application uptime. Spreading the logic across multiple internal services and containerizing it with Docker, this microservice solves the issue by simplifying implementation to database hook up only and allowing developers to spin up an new instances for updates with active user routing only after approval.

For a live demo, click here!


The Stack

Language: Python
Package Manager: uv
Framework: FastAPI
Server Runtime: uvicorn
Hashing/Salting: bcrypt
Validator: Pydantic
ORM: SQLAlchemy
Database: SQLite 3
Containerization: Docker


What This Build Has Taught Me

Making code that is both user and developer-friendly 
Choose between Flask and FastAPI
ORM vs crude SQL query
MySQL vs SQLite vs Postgres
Commenting best practices for readability


Get Started

Python --version

git clone or GitHub

Reminder

Make adjustments to [insert file here] to connect a database of your choosing (e.g. Postgres, MySQL, cloud database). Additionally, please be sure to make appriopriate changes to the unit tests to reflect the new database connections.