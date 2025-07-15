# Metric Calorie Calculator

## Overview

A simple web application that calculates your daily calorie needs (BMR and TDEE) along with macronutrient distribution, using metric units (cm, kg).

## Features

- Calculates Basal Metabolic Rate (BMR) using Mifflin-St Jeor equation
- Estimates Total Daily Energy Expenditure (TDEE) based on activity level
- Provides macronutrient breakdown (30% protein, 40% carbs, 30% fat)
- Clean, responsive interface
- Metric units only (centimeters and kilograms)

## Installation

1. Clone this repository or download the files
2. Ensure you have Python 3.x installed
3. Install Flask:
   ```
   pip install flask
   ```

## Usage

1. Run the application:
   ```
   python app.py
   ```
2. Open your web browser to:
   ```
   http://localhost:5000
   ```
3. Fill in your information:
   - Age (15-80 years)
   - Gender
   - Height (cm)
   - Weight (kg)
   - Activity level
4. Click "Calculate" to see your results

## File Structure

```
metric-calorie-calculator/
├── app.py               # Flask backend
└── static/
    └── index.html       # Frontend HTML/CSS/JS
```

## API Endpoints

- `POST /calculate` - Receives user data and returns calculations
  - Required JSON payload:
    ```json
    {
      "age": number,
      "gender": "male"|"female",
      "height": number,
      "weight": number,
      "activity_level": number
    }
    ```

## Calculations

- **BMR** (Basal Metabolic Rate): Calculated using Mifflin-St Jeor equation
- **TDEE**: BMR × Activity Level multiplier
- **Macronutrients**:
  - Protein: 30% of TDEE (4 calories/gram)
  - Carbohydrates: 40% of TDEE (4 calories/gram)
  - Fat: 30% of TDEE (9 calories/gram)

## Activity Level Multipliers

1. Sedentary (little or no exercise): 1.2
2. Light (exercise 1-3 times/week): 1.375
3. Moderate (exercise 4-5 times/week): 1.55
4. Active (intense exercise 6-7 times/week): 1.725
5. Very Active (very intense exercise & physical job): 1.9

## License

This project is open source and available under the MIT License.

## Interface
<img width="530" height="500" alt="Interface" src="https://github.com/user-attachments/assets/0375081e-e2bf-4395-b6e1-eabbd81e2514" />

# Results
<img width="951" height="567" alt="Results" src="https://github.com/user-attachments/assets/398b5ec0-3985-4620-85b4-eb8078ced4ee" />
