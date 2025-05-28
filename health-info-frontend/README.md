# Health Information Frontend

This project is a simple frontend application built with TypeScript and React to visualize the health information system data from the Django backend.

## Project Structure

```
health-info-frontend
├── src
│   ├── index.ts          # Entry point of the application
│   ├── components
│   │   └── App.tsx       # Main App component
│   ├── styles
│   │   └── App.css       # Styles for the App component
│   └── types
│       └── index.ts      # TypeScript interfaces and types
├── public
│   └── index.html        # Main HTML template
├── package.json          # npm configuration file
├── tsconfig.json         # TypeScript configuration file
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd health-info-frontend
   ```

2. **Install dependencies:**
   ```
   npm install
   ```

3. **Run the application:**
   ```
   npm start
   ```

4. **Build the application for production:**
   ```
   npm run build
   ```

## Usage Guidelines

- The application connects to the Django backend to fetch health information data.
- Modify the `src/components/App.tsx` file to customize the visualization of the data.
- Update the `src/types/index.ts` file to define any new types or interfaces as needed.

## License

This project is licensed under the MIT License.