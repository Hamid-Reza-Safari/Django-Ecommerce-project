### Project Structure:
The project is structured within the `store` directory, encompassing two distinct Django apps:

1. **shop**:
   The `shop` app serves as the core component handling product management and user interaction. Key functionalities and files include:
   - `forms.py`: Implements user authentication forms for login and registration.
   - `views.py`: Contains logic for user authentication, product browsing, cart management, and order processing.
   - `urls.py`: Manages URL routing for different pages, such as product details, login, and category listings.
   - `models.py`: Defines database models such as `Product`, `Customer`, and `Category` to facilitate data storage and retrieval.

2. **cart**:
   The `cart` app focuses specifically on cart-related functionalities, allowing users to add, remove, and adjust quantities of items in their shopping cart.

### Database:
SQLite3 was chosen as the database backend for its simplicity and seamless integration with Django. While SQLite3 is ideal for development purposes and smaller-scale applications, Django's ORM (Object-Relational Mapping) ensures compatibility with other database systems like PostgreSQL or MySQL for future scalability.

### Frontend Technologies:
The frontend of the ecommerce platform is developed using:
- **HTML5**: Provides the structure and layout of webpages.
- **CSS**: Handles the styling and visual presentation of the site.
- **JavaScript**: Enhances user interactions and dynamic features, though the primary focus remains on backend development with Python and Django.

### Features:
#### User-Side Functionality:
- **User Authentication**:
  - Users can register new accounts and securely log in using encrypted credentials. User data, including profile information and order history, is stored in the database.
- **Product Interaction**:
  - Each product has a dedicated page displaying detailed information and pricing. Users can add items to their shopping cart and adjust quantities as needed.
  - The cart management system allows users to review, modify, and remove items before proceeding to checkout.

#### Admin-Side Functionality:
- **Admin Dashboard**:
  - Administrators have access to a comprehensive dashboard for managing the ecommerce platform. They can add new product categories, create, edit, or delete products, and oversee user accounts and orders.
- **Product Management**:
  - Products can be assigned to specific categories and tagged with relevant attributes. Admins can enable discounts by setting percentage-based offers on individual products.
- **User Management**:
  - Admins have authority over user accounts, including permission settings and user profile editing capabilities.
- **Order Management**:
  - The admin panel provides a centralized view of all orders placed on the website, allowing administrators to track, update, and manage order statuses efficiently.

### Design Considerations:
- **Database Choice**:
  - SQLite3 was selected primarily for its ease of setup and usage during development. The decision was influenced by the project's scope and anticipated scale.
- **Frontend vs. Backend Focus**:
  - While frontend technologies are used to enhance user experience, the project's primary emphasis remains on robust backend functionalities. Django's MVC (Model-View-Controller) architecture ensures a clear separation of concerns, facilitating efficient development and maintenance.

### Additional Notes:
Despite the initial naming convention (`store` folder), the project encapsulates a comprehensive ecommerce solution, emphasizing functionality and user experience. Future iterations could explore additional features such as payment integration, enhanced product search capabilities, and responsive design for optimal cross-device compatibility.
