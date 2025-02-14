# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime

engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base = declarative_base()

# Data Models

class Dealership(Base):
    """description: Represents a car dealership entity."""
    __tablename__ = 'dealership'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String)
    
class CarModel(Base):
    """description: Represents different car models available at the dealership."""
    __tablename__ = 'car_model'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    manufacturer = Column(String)
    
class Car(Base):
    """description: Represents individual cars in the inventory."""
    __tablename__ = 'car'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    vin = Column(String, unique=True, nullable=False)
    model_id = Column(Integer, ForeignKey('car_model.id'))
    dealership_id = Column(Integer, ForeignKey('dealership.id'))
    year = Column(Integer)
    price = Column(Float)
    
class Customer(Base):
    """description: Represents customers of the dealership."""
    __tablename__ = 'customer'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String)
    
class Sale(Base):
    """description: Represents sales transactions at the dealership."""
    __tablename__ = 'sale'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('car.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))
    sale_date = Column(Date, default=datetime.date.today)
    sale_price = Column(Float)
    
class Service(Base):
    """description: Represents services offered by the dealership's service department."""
    __tablename__ = 'service'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('car.id'))
    date = Column(Date, default=datetime.date.today)
    description = Column(String)
    cost = Column(Float)
    
class Employee(Base):
    """description: Represents employees working at the dealership."""
    __tablename__ = 'employee'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    role = Column(String)
    hire_date = Column(Date)
    salary = Column(Float)
    
class Appointment(Base):
    """description: Represents appointments made by customers for car services."""
    __tablename__ = 'appointment'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    service_id = Column(Integer, ForeignKey('service.id'))
    appointment_date = Column(Date)
    is_confirmed = Column(Boolean, default=False)
    
class Review(Base):
    """description: Represents customer reviews for the cars."""
    __tablename__ = 'review'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    car_id = Column(Integer, ForeignKey('car.id'))
    rating = Column(Integer)
    comment = Column(String)
    
class Manufacturer(Base):
    """description: Represents car manufacturers."""
    __tablename__ = 'manufacturer'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    origin_country = Column(String)

class Inventory(Base):
    """description: Represents current status of cars available in the warehouse."""
    __tablename__ = 'inventory'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('car.id'))
    quantity = Column(Integer, nullable=False, default=0)
    
class Accessory(Base):
    """description: Represents car accessories available in the dealership."""
    __tablename__ = 'accessory'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float)
    
# Create tables
Base.metadata.create_all(engine)

# Sample Data
Session = sessionmaker(bind=engine)
session = Session()

# Creating sample data for each table

# Dealerships
dealership1 = Dealership(name="North End Motors", location="Boston, MA")
dealership2 = Dealership(name="AutoPlus Store", location="Chicago, IL")
session.add(dealership1)
session.add(dealership2)

# Car Models
model1 = CarModel(name="Model S", manufacturer="Tesla")
model2 = CarModel(name="Civic", manufacturer="Honda")
model3 = CarModel(name="Corolla", manufacturer="Toyota")
session.add_all([model1, model2, model3])

# Cars
car1 = Car(vin="1HGBH41JXMN109186", model_id=1, dealership_id=1, year=2020, price=35000)
car2 = Car(vin="JHMZF1D63CS004837", model_id=2, dealership_id=1, year=2019, price=22000)
car3 = Car(vin="JTDBR32E330056620", model_id=3, dealership_id=2, year=2021, price=18000)
session.add_all([car1, car2, car3])

# Customers
customer1 = Customer(first_name="John", last_name="Doe", phone_number="555-1234")
customer2 = Customer(first_name="Jane", last_name="Smith", phone_number="555-5678")
session.add_all([customer1, customer2])

# Sales
sale1 = Sale(car_id=1, customer_id=1, sale_price=34500)
sale2 = Sale(car_id=2, customer_id=2, sale_price=21500)
session.add_all([sale1, sale2])

# Services
service1 = Service(car_id=1, description="Oil Change", cost=100)
service2 = Service(car_id=2, description="Brake Repair", cost=200)
session.add_all([service1, service2])

# Employees
employee1 = Employee(first_name="Alice", last_name="Johnson", role="Sales Manager", hire_date=datetime.date(2021, 5, 1), salary=70000)
employee2 = Employee(first_name="Bob", last_name="Brown", role="Technician", hire_date=datetime.date(2020, 3, 15), salary=50000)
session.add_all([employee1, employee2])

# Appointments
appointment1 = Appointment(customer_id=1, service_id=1, appointment_date=datetime.date(2023, 11, 10), is_confirmed=True)
appointment2 = Appointment(customer_id=2, service_id=2, appointment_date=datetime.date(2023, 11, 15), is_confirmed=False)
session.add_all([appointment1, appointment2])

# Reviews
review1 = Review(customer_id=1, car_id=1, rating=5, comment="Excellent performance!")
review2 = Review(customer_id=2, car_id=2, rating=4, comment="Good value for money.")
session.add_all([review1, review2])

# Manufacturers
manufacturer1 = Manufacturer(name="Tesla", origin_country="USA")
manufacturer2 = Manufacturer(name="Honda", origin_country="Japan")
manufacturer3 = Manufacturer(name="Toyota", origin_country="Japan")
session.add_all([manufacturer1, manufacturer2, manufacturer3])

# Inventory
inventory1 = Inventory(car_id=1, quantity=5)
inventory2 = Inventory(car_id=2, quantity=8)
session.add_all([inventory1, inventory2])

# Accessories
accessory1 = Accessory(name="Sunroof", price=1200)
accessory2 = Accessory(name="Leather seats", price=1500)
session.add_all([accessory1, accessory2])

# Commit the session
session.commit()
