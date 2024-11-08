import { MenuRootItem } from 'ontimize-web-ngx';

import { AccessoryCardComponent } from './Accessory-card/Accessory-card.component';

import { AppointmentCardComponent } from './Appointment-card/Appointment-card.component';

import { CarCardComponent } from './Car-card/Car-card.component';

import { CarModelCardComponent } from './CarModel-card/CarModel-card.component';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { DealershipCardComponent } from './Dealership-card/Dealership-card.component';

import { EmployeeCardComponent } from './Employee-card/Employee-card.component';

import { InventoryCardComponent } from './Inventory-card/Inventory-card.component';

import { ManufacturerCardComponent } from './Manufacturer-card/Manufacturer-card.component';

import { ReviewCardComponent } from './Review-card/Review-card.component';

import { SaleCardComponent } from './Sale-card/Sale-card.component';

import { ServiceCardComponent } from './Service-card/Service-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Accessory', name: 'ACCESSORY', icon: 'view_list', route: '/main/Accessory' }
    
        ,{ id: 'Appointment', name: 'APPOINTMENT', icon: 'view_list', route: '/main/Appointment' }
    
        ,{ id: 'Car', name: 'CAR', icon: 'view_list', route: '/main/Car' }
    
        ,{ id: 'CarModel', name: 'CARMODEL', icon: 'view_list', route: '/main/CarModel' }
    
        ,{ id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Dealership', name: 'DEALERSHIP', icon: 'view_list', route: '/main/Dealership' }
    
        ,{ id: 'Employee', name: 'EMPLOYEE', icon: 'view_list', route: '/main/Employee' }
    
        ,{ id: 'Inventory', name: 'INVENTORY', icon: 'view_list', route: '/main/Inventory' }
    
        ,{ id: 'Manufacturer', name: 'MANUFACTURER', icon: 'view_list', route: '/main/Manufacturer' }
    
        ,{ id: 'Review', name: 'REVIEW', icon: 'view_list', route: '/main/Review' }
    
        ,{ id: 'Sale', name: 'SALE', icon: 'view_list', route: '/main/Sale' }
    
        ,{ id: 'Service', name: 'SERVICE', icon: 'view_list', route: '/main/Service' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AccessoryCardComponent

    ,AppointmentCardComponent

    ,CarCardComponent

    ,CarModelCardComponent

    ,CustomerCardComponent

    ,DealershipCardComponent

    ,EmployeeCardComponent

    ,InventoryCardComponent

    ,ManufacturerCardComponent

    ,ReviewCardComponent

    ,SaleCardComponent

    ,ServiceCardComponent

];