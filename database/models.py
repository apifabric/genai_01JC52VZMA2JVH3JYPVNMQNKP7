# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 08, 2024 05:10:39
# Database: sqlite:////tmp/tmp.dvvjU67Y08/genai_01JC52VZMA2JVH3JYPVNMQNKP7/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Accessory(SAFRSBaseX, Base):
    """
    description: Represents car accessories available in the dealership.
    """
    __tablename__ = 'accessory'
    _s_collection_name = 'Accessory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float)

    # parent relationships (access parent)

    # child relationships (access children)



class CarModel(SAFRSBaseX, Base):
    """
    description: Represents different car models available at the dealership.
    """
    __tablename__ = 'car_model'
    _s_collection_name = 'CarModel'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    manufacturer = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    CarList : Mapped[List["Car"]] = relationship(back_populates="model")



class Customer(SAFRSBaseX, Base):
    """
    description: Represents customers of the dealership.
    """
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="customer")
    SaleList : Mapped[List["Sale"]] = relationship(back_populates="customer")
    AppointmentList : Mapped[List["Appointment"]] = relationship(back_populates="customer")



class Dealership(SAFRSBaseX, Base):
    """
    description: Represents a car dealership entity.
    """
    __tablename__ = 'dealership'
    _s_collection_name = 'Dealership'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    CarList : Mapped[List["Car"]] = relationship(back_populates="dealership")



class Employee(SAFRSBaseX, Base):
    """
    description: Represents employees working at the dealership.
    """
    __tablename__ = 'employee'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    role = Column(String)
    hire_date = Column(Date)
    salary = Column(Float)

    # parent relationships (access parent)

    # child relationships (access children)



class Manufacturer(SAFRSBaseX, Base):
    """
    description: Represents car manufacturers.
    """
    __tablename__ = 'manufacturer'
    _s_collection_name = 'Manufacturer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    origin_country = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)



class Car(SAFRSBaseX, Base):
    """
    description: Represents individual cars in the inventory.
    """
    __tablename__ = 'car'
    _s_collection_name = 'Car'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    vin = Column(String, nullable=False, unique=True)
    model_id = Column(ForeignKey('car_model.id'))
    dealership_id = Column(ForeignKey('dealership.id'))
    year = Column(Integer)
    price = Column(Float)

    # parent relationships (access parent)
    dealership : Mapped["Dealership"] = relationship(back_populates=("CarList"))
    model : Mapped["CarModel"] = relationship(back_populates=("CarList"))

    # child relationships (access children)
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="car")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="car")
    SaleList : Mapped[List["Sale"]] = relationship(back_populates="car")
    ServiceList : Mapped[List["Service"]] = relationship(back_populates="car")



class Inventory(SAFRSBaseX, Base):
    """
    description: Represents current status of cars available in the warehouse.
    """
    __tablename__ = 'inventory'
    _s_collection_name = 'Inventory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    car_id = Column(ForeignKey('car.id'))
    quantity = Column(Integer, nullable=False)

    # parent relationships (access parent)
    car : Mapped["Car"] = relationship(back_populates=("InventoryList"))

    # child relationships (access children)



class Review(SAFRSBaseX, Base):
    """
    description: Represents customer reviews for the cars.
    """
    __tablename__ = 'review'
    _s_collection_name = 'Review'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'))
    car_id = Column(ForeignKey('car.id'))
    rating = Column(Integer)
    comment = Column(String)

    # parent relationships (access parent)
    car : Mapped["Car"] = relationship(back_populates=("ReviewList"))
    customer : Mapped["Customer"] = relationship(back_populates=("ReviewList"))

    # child relationships (access children)



class Sale(SAFRSBaseX, Base):
    """
    description: Represents sales transactions at the dealership.
    """
    __tablename__ = 'sale'
    _s_collection_name = 'Sale'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    car_id = Column(ForeignKey('car.id'))
    customer_id = Column(ForeignKey('customer.id'))
    sale_date = Column(Date)
    sale_price = Column(Float)

    # parent relationships (access parent)
    car : Mapped["Car"] = relationship(back_populates=("SaleList"))
    customer : Mapped["Customer"] = relationship(back_populates=("SaleList"))

    # child relationships (access children)



class Service(SAFRSBaseX, Base):
    """
    description: Represents services offered by the dealership's service department.
    """
    __tablename__ = 'service'
    _s_collection_name = 'Service'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    car_id = Column(ForeignKey('car.id'))
    date = Column(Date)
    description = Column(String)
    cost = Column(Float)

    # parent relationships (access parent)
    car : Mapped["Car"] = relationship(back_populates=("ServiceList"))

    # child relationships (access children)
    AppointmentList : Mapped[List["Appointment"]] = relationship(back_populates="service")



class Appointment(SAFRSBaseX, Base):
    """
    description: Represents appointments made by customers for car services.
    """
    __tablename__ = 'appointment'
    _s_collection_name = 'Appointment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'))
    service_id = Column(ForeignKey('service.id'))
    appointment_date = Column(Date)
    is_confirmed = Column(Boolean)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("AppointmentList"))
    service : Mapped["Service"] = relationship(back_populates=("AppointmentList"))

    # child relationships (access children)
