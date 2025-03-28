from datetime import date, timedelta
from typing import Dict, List, Optional


# Base class for Person
class Person:
    def __init__(self, personId: int, name: str, email: str, phone: str):
        self.personId = personId
        self.name = name
        self.email = email
        self.phone = phone

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name

    def getEmail(self) -> str:
        return self.email

    def setEmail(self, email: str) -> None:
        self.email = email

    def getPhone(self) -> str:
        return self.phone

    def setPhone(self, phone: str) -> None:
        self.phone = phone

    def __str__(self) -> str:
        return f"Person: {self.name}, Email: {self.email}, Phone: {self.phone}"


# Employee class inherits from Person
class Employee(Person):
    def __init__(self, personId: int, name: str, email: str, phone: str, position: str, salary: float):
        super().__init__(personId, name, email, phone)
        self.position = position
        self.salary = salary
        self.joiningDate = date.today()

    def assignTasks(self, tasks: List[str]) -> bool:
        # Implementation to assign tasks to employee
        return True

    def processRequest(self, request: str) -> bool:
        # Implementation to process a guest request
        return True

    def __str__(self) -> str:
        return f"Employee: {self.name}, Position: {self.position}, Salary: ${self.salary}"


# Manager class inherits from Employee
class Manager(Employee):
    def __init__(self, personId: int, name: str, email: str, phone: str, salary: float, department: str):
        super().__init__(personId, name, email, phone, "Manager", salary)
        self.department = department
        self.subordinates: List[Employee] = []

    def addSubordinate(self, employee: Employee) -> bool:
        if employee not in self.subordinates:
            self.subordinates.append(employee)
            return True
        return False

    def removeSubordinate(self, employee: Employee) -> bool:
        if employee in self.subordinates:
            self.subordinates.remove(employee)
            return True
        return False

    def approveBudget(self, amount: float, reason: str) -> bool:
        # Implementation to approve budget requests
        return True

    def evaluateStaff(self, employee: Employee, rating: int, comments: str) -> bool:
        # Implementation to evaluate staff performance
        return True

    def __str__(self) -> str:
        return f"Manager: {self.name}, Department: {self.department}, Subordinates: {len(self.subordinates)}"


# Base Room class
class Room:
    def __init__(self, roomNumber: int, roomType: str, amenities: List[str], pricePerNight: float, isAvailable: bool):
        self.roomNumber = roomNumber
        self.roomType = roomType
        self.amenities = amenities
        self.pricePerNight = pricePerNight
        self.isAvailable = isAvailable

    def updateStatus(self, isAvailable: bool) -> bool:
        self.isAvailable = isAvailable
        return True

    def updatePrice(self, price: float) -> bool:
        self.pricePerNight = price
        return True

    def addAmenity(self, amenity: str) -> bool:
        if amenity not in self.amenities:
            self.amenities.append(amenity)
            return True
        return False

    def removeAmenity(self, amenity: str) -> bool:
        if amenity in self.amenities:
            self.amenities.remove(amenity)
            return True
        return False

    def __str__(self) -> str:
        status = "Available" if self.isAvailable else "Occupied"
        return f"Room {self.roomNumber}: {self.roomType}, ${self.pricePerNight}/night, Status: {status}"


# SingleRoom class inherits from Room
class SingleRoom(Room):
    def __init__(self, roomNumber: int, roomType: str, amenities: List[str], pricePerNight: float,
                 isAvailable: bool, isSingleBed: bool, maxOccupancy: int, hasWorkDesk: bool):
        super().__init__(roomNumber, roomType, amenities, pricePerNight, isAvailable)
        self.isSingleBed = isSingleBed
        self.maxOccupancy = maxOccupancy
        self.hasWorkDesk = hasWorkDesk

    def setUpForBusiness(self) -> bool:
        # Implementation to set up room for business travelers
        self.hasWorkDesk = True
        if "Work Lamp" not in self.amenities:
            self.amenities.append("Work Lamp")
        return True

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str}, Single Bed: {self.isSingleBed}, Max Occupancy: {self.maxOccupancy}"


# DoubleRoom class inherits from Room
class DoubleRoom(Room):
    def __init__(self, roomNumber: int, roomType: str, amenities: List[str], pricePerNight: float,
                 isAvailable: bool, numberOfBeds: int, hasBalcony: bool, isConnected: bool):
        super().__init__(roomNumber, roomType, amenities, pricePerNight, isAvailable)
        self.numberOfBeds = numberOfBeds
        self.hasBalcony = hasBalcony
        self.isConnected = isConnected

    def seperateBeds(self) -> bool:
        # Implementation to separate beds (note: typo from class diagram preserved)
        return True

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str}, Beds: {self.numberOfBeds}, Balcony: {self.hasBalcony}"


# SuiteRoom class inherits from Room
class SuiteRoom(Room):
    def __init__(self, roomNumber: int, roomType: str, amenities: List[str], pricePerNight: float,
                 isAvailable: bool, numberOfRooms: int, hasKitchen: bool, hasJacuzzi: bool):
        super().__init__(roomNumber, roomType, amenities, pricePerNight, isAvailable)
        self.numberOfRooms = numberOfRooms
        self.hasKitchen = hasKitchen
        self.hasJacuzzi = hasJacuzzi

    def arrangeSpecialService(self) -> bool:
        # Implementation to arrange special services for suite guests
        return True

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str}, Number of Rooms: {self.numberOfRooms}, Kitchen: {self.hasKitchen}, Jacuzzi: {self.hasJacuzzi}"


# Guest class inherits from Person
class Guest(Person):
    def __init__(self, personId: int, name: str, email: str, phone: str):
        super().__init__(personId, name, email, phone)
        self.loyaltyPoints = 0
        self.loyaltyStatus = "Regular"
        self.bookingHistory: List[Booking] = []

    def createAccount(self) -> bool:
        # Implementation for creating a guest account
        return True

    def updateProfile(self, name: str, email: str, phone: str) -> bool:
        self.setName(name)
        self.setEmail(email)
        self.setPhone(phone)
        return True

    def viewReservationHistory(self) -> List['Booking']:
        return self.bookingHistory

    def earnPoints(self, points: int) -> int:
        self.loyaltyPoints += points
        return self.loyaltyPoints

    def redeemPoints(self, points: int) -> bool:
        if self.loyaltyPoints >= points:
            self.loyaltyPoints -= points
            return True
        return False

    def __str__(self) -> str:
        return f"Guest: {self.name}, Status: {self.loyaltyStatus}, Points: {self.loyaltyPoints}"


# Service class
class Service:
    def __init__(self, serviceId: int, serviceType: str, description: str, price: float):
        self.serviceId = serviceId
        self.serviceType = serviceType
        self.description = description
        self.price = price
        self.status = "Requested"
        self.requestTime = date.today()
        self.completionTime = None

    def createRequest(self, guest: Guest, booking: 'Booking') -> bool:
        # Implementation for creating a service request
        return True

    def updateStatus(self, status: str) -> bool:
        self.status = status
        if status == "Completed":
            self.completionTime = date.today()
        return True

    def calculatePrice(self, quantity: int, basePrice: float) -> float:
        return quantity * basePrice

    def __str__(self) -> str:
        return f"Service: {self.serviceType}, Description: {self.description}, Price: ${self.price}, Status: {self.status}"


# Booking class
class Booking:
    def __init__(self, bookingId: int, guest: Guest, room: Room, checkInDate: date, checkOutDate: date):
        self.bookingId = bookingId
        self.guest = guest
        self.room = room
        self.checkInDate = checkInDate
        self.checkOutDate = checkOutDate
        self.totalPrice = self.calculateTotalPrice()
        self.status = "Confirmed"
        self.services: List[Service] = []

        # Mark room as unavailable
        room.updateStatus(False)

    def calculateTotalPrice(self) -> float:
        # Calculate number of nights
        if self.checkInDate and self.checkOutDate:
            days = (self.checkOutDate - self.checkInDate).days
            base_price = days * self.room.pricePerNight

            # Add cost of services
            service_cost = sum(service.price for service in self.services)

            return base_price + service_cost
        return 0

    def cancel(self) -> bool:
        if self.status == "Confirmed":
            self.status = "Cancelled"
            self.room.updateStatus(True)  # Make room available again
            return True
        return False

    def complete(self) -> bool:
        if self.status == "Confirmed":
            self.status = "Completed"
            self.room.updateStatus(True)  # Make room available again
            return True
        return False

    def sendConfirmation(self) -> bool:
        if self.status == "Cancelled":
            return False

        if not self.checkInDate or not self.checkOutDate:
            raise ValueError("Booking dates are missing")

        # Implementation to send confirmation email/notification
        return True

    def __str__(self) -> str:
        return (f"Booking ID: {self.bookingId}, Guest: {self.guest.getName()}, "
                f"Room: {self.room.roomNumber}, Check-in: {self.checkInDate}, "
                f"Check-out: {self.checkOutDate}, Status: {self.status}, "
                f"Total: ${self.totalPrice}")


# Payment class
class Payment:
    def __init__(self, paymentId: int, amount: float, paymentDate: date, paymentMethod: str, status: str):
        self.paymentId = paymentId
        self.amount = amount
        self.paymentDate = paymentDate
        self.paymentMethod = paymentMethod
        self.status = status

    def processPayment(self) -> bool:
        # Implementation to process payment
        self.status = "Completed"
        return True

    def generateReceipt(self) -> str:
        # Implementation to generate payment receipt
        receipt = (f"Receipt #{self.paymentId}\n"
                   f"Amount: ${self.amount}\n"
                   f"Date: {self.paymentDate}\n"
                   f"Method: {self.paymentMethod}\n"
                   f"Status: {self.status}")
        return receipt

    def refund(self, amount: float) -> bool:
        # Implementation to process refund
        if amount <= 0:
            return False

        if amount == self.amount:
            self.status = "Refunded"
        else:
            self.status = "Partially Refunded"

        return True

    def __str__(self) -> str:
        return f"Payment {self.paymentId}: ${self.amount}, Method: {self.paymentMethod}, Status: {self.status}"


# Invoice class
class Invoice:
    def __init__(self, invoiceId: int, invoiceDate: date, subtotal: float, tax: float, discount: float,
                 finalAmount: float = 0):
        self.invoiceId = invoiceId
        self.invoiceDate = invoiceDate
        self.subtotal = subtotal
        self.tax = tax  # Tax rate (e.g., 0.08 for 8%)
        self.discount = discount  # Discount rate (e.g., 0.1 for 10%)
        self.finalAmount = finalAmount if finalAmount > 0 else self.calculateTotal()

    def calculateTotal(self) -> float:
        # Apply discount to subtotal
        discounted_amount = self.applyDiscount(self.subtotal, self.discount)

        # Apply tax to discounted amount
        tax_amount = discounted_amount * self.tax

        # Calculate final amount
        self.finalAmount = discounted_amount + tax_amount
        return self.finalAmount

    def applyDiscount(self, amount: float, discountRate: float) -> float:
        return amount * (1 - discountRate)

    def generateInvoice(self) -> str:
        # Implementation to generate invoice document
        invoice = (f"Invoice #{self.invoiceId}\n"
                   f"Date: {self.invoiceDate}\n"
                   f"Subtotal: ${self.subtotal:.2f}\n"
                   f"Discount: {self.discount * 100:.0f}%\n"
                   f"Tax: {self.tax * 100:.0f}%\n"
                   f"Total: ${self.finalAmount:.2f}")
        return invoice

    def __str__(self) -> str:
        return f"Invoice {self.invoiceId}: ${self.finalAmount}, Date: {self.invoiceDate}"


# LoyaltyProgram class
class LoyaltyProgram:
    def __init__(self, pointsScheme: Dict[str, float], statusThresholds: Dict[str, int],
                 rewardOptions: Dict[str, Dict]):
        self.pointsScheme = pointsScheme
        self.statusThresholds = statusThresholds
        self.rewardOptions = rewardOptions

    def calculatePoints(self, amount: float, transactionType: str) -> int:
        if transactionType in self.pointsScheme:
            # Calculate points as percentage of transaction amount
            points_rate = self.pointsScheme[transactionType] / 100.0
            return int(amount * points_rate)
        return 0

    def determineStatus(self, points: int) -> str:
        # Determine guest status based on points
        status = "Regular"

        for status_level, threshold in sorted(self.statusThresholds.items(), key=lambda x: x[1]):
            if points >= threshold:
                status = status_level
            else:
                break

        return status

    def getAvailableRewards(self, points: int) -> Dict:
        # Return rewards available based on points and status
        status = self.determineStatus(points)
        available_rewards = {}

        # Add rewards for current status and below
        for status_level, rewards in self.rewardOptions.items():
            if status_level == status:
                for reward_name, reward_cost in rewards.items():
                    if points >= reward_cost:
                        available_rewards[reward_name] = reward_cost

        return available_rewards

    def redeemReward(self, guest: Guest, rewardName: str) -> bool:
        # Find reward and its cost
        rewards = self.getAvailableRewards(guest.loyaltyPoints)

        if rewardName in rewards:
            cost = rewards[rewardName]
            # Attempt to redeem points
            return guest.redeemPoints(cost)

        return False

    def __str__(self) -> str:
        status_levels = ", ".join(self.statusThresholds.keys())
        return f"Loyalty Program: Status Levels: {status_levels}"


# Main HotelSystem class
class HotelSystem:
    def __init__(self):
        self.rooms: Dict[int, Room] = {}
        self.services: Dict[int, Service] = {}
        self.guests: Dict[int, Guest] = {}
        self.employees: Dict[int, Employee] = {}
        self.bookings: Dict[int, Booking] = {}
        self.payments: Dict[int, Payment] = {}
        self.invoices: Dict[int, Invoice] = {}
        self.loyaltyProgram = None

        # Counter for generating IDs
        self._next_person_id = 1
        self._next_service_id = 1
        self._next_booking_id = 1
        self._next_payment_id = 1
        self._next_invoice_id = 1

    def addRoom(self, room: Room) -> bool:
        if room.roomNumber not in self.rooms:
            self.rooms[room.roomNumber] = room
            return True
        return False

    def removeRoom(self, roomNumber: int) -> bool:
        if roomNumber in self.rooms:
            del self.rooms[roomNumber]
            return True
        return False

    def registerGuest(self, name: str, email: str, phone: str) -> Guest:
        # Validate inputs
        if not email:
            raise ValueError("Email cannot be empty")

        # Simple validation for phone
        if not phone or len(phone) < 7:
            raise ValueError("Invalid phone number")

        guest_id = self._next_person_id
        self._next_person_id += 1

        guest = Guest(guest_id, name, email, phone)
        self.guests[guest_id] = guest
        return guest

    def hireEmployee(self, name: str, email: str, phone: str, position: str, salary: float) -> Employee:
        employee_id = self._next_person_id
        self._next_person_id += 1

        employee = Employee(employee_id, name, email, phone, position, salary)
        self.employees[employee_id] = employee
        return employee

    def hireManager(self, name: str, email: str, phone: str, salary: float, department: str) -> Manager:
        manager_id = self._next_person_id
        self._next_person_id += 1

        manager = Manager(manager_id, name, email, phone, salary, department)
        self.employees[manager_id] = manager
        return manager

    def findAvailableRooms(self, checkInDate: date, checkOutDate: date, roomType: Optional[str] = None) -> List[Room]:
        # Validate dates
        if checkInDate >= checkOutDate:
            raise ValueError("Check-out date must be after check-in date")

        available_rooms = []

        for room in self.rooms.values():
            if room.isAvailable:
                if roomType is None or room.roomType == roomType:
                    available_rooms.append(room)

        return available_rooms

    def makeBooking(self, guest: Guest, room: Room, checkInDate: date, checkOutDate: date) -> Booking:
        # Validate dates
        if checkInDate >= checkOutDate:
            raise ValueError("Check-out date must be after check-in date")

        # Check if room is available
        if not room.isAvailable:
            raise ValueError(f"Room {room.roomNumber} is not available for the selected dates")

        booking_id = self._next_booking_id
        self._next_booking_id += 1

        booking = Booking(booking_id, guest, room, checkInDate, checkOutDate)
        self.bookings[booking_id] = booking

        return booking

    def requestService(self, guest: Guest, serviceType: str, description: str, price: float,
                       booking: Booking) -> Service:
        service_id = self._next_service_id
        self._next_service_id += 1

        service = Service(service_id, serviceType, description, price)
        service.createRequest(guest, booking)

        self.services[service_id] = service
        return service

    def __str__(self) -> str:
        return (f"Hotel System: {len(self.rooms)} rooms, {len(self.guests)} guests, "
                f"{len(self.employees)} employees, {len(self.bookings)} bookings")


# Test code
if __name__ == "__main__":
    # Just a simple test to ensure the file runs
    hotel = HotelSystem()
    print("Hotel system initialized successfully!")