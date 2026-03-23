# README

## Project Title

CONSUMO ENERGIA

## Description

This project aims to analyze and calculate energy consumption. It provides an algorithm to calculate energy consumption based on various factors such as usage time, appliance wattage, and cost rate. The following is a breakdown of the algorithm used:

### Algorithm Description
1. **Inputs:**
   - `appliance_wattage`: The power rating of the appliance in watts.
   - `usage_time`: The time the appliance is used in hours.
   - `cost_rate`: The cost of electricity per kWh.

2. **Steps:**
   1. Calculate energy consumed (in kWh): 
      
      \[ \text{Energy (kWh)} = \frac{\text{Appliance Wattage (W)} \times \text{Usage Time (h)}}{1000} \]
      
   2. Calculate total cost:
      
      \[ \text{Total Cost} = \text{Energy (kWh)} \times \text{Cost Rate (per kWh)} \]
      
3. **Outputs:**
   - Total energy consumption in kWh.
   - Total cost for the energy consumed.

### Example
- If an appliance with a power rating of 1000W is used for 5 hours at a cost rate of $0.12 per kWh:
  - Energy consumed: 5 kWh
  - Total cost: $0.60

## Installation

Clone the repository:

```bash
git clone https://github.com/VPS-F01/CONSUMO-ENERGIA.git
```

## Usage

Run the main script to start the program.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to all contributors and resources used in this project.