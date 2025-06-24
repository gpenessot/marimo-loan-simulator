# 🏠 Marimo Loan Simulator

Interactive loan simulator built with Marimo - multi-scenario comparison with reactive charts and instant web app deployment

[![Marimo](https://img.shields.io/badge/Built%20with-Marimo-blue)](https://marimo.io)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 Features

- **Multi-scenario comparison**: Compare up to 3 loan scenarios side by side
- **Reactive interface**: Real-time updates when you modify parameters
- **Interactive charts**: Capital remaining, cumulative interest, monthly breakdown
- **Professional calculations**: Accurate amortization schedules with insurance
- **Data export**: Generate CSV files for external analysis
- **Instant deployment**: Transform notebook to web app with one command
- **Pure Python**: Git-friendly storage, no JSON conflicts

## 📊 What You'll Build

This simulator demonstrates Marimo's key capabilities:

- **Reactive programming**: Change a parameter, see all dependent calculations update instantly
- **Native UI components**: Sliders, dropdowns, and forms without callback hell
- **Seamless deployment**: Same code works as notebook and web application
- **SQL integration**: Query and transform data with built-in SQL cells
- **Professional interface**: Production-ready styling and layout

## 🛠️ Quick Start

### Prerequisites

- Python 3.8+
- pip or conda

### Installation

```bash
# Install Marimo with all dependencies
pip install marimo[sql]

# Clone this repository
git clone https://github.com/yourusername/marimo-loan-simulator.git
cd marimo-loan-simulator
```

### Running the Simulator

**As Interactive Notebook:**
```bash
marimo edit loan_simulator.py
```

**As Web Application:**
```bash
marimo run loan_simulator.py
```

**As Python Script:**
```bash
python loan_simulator.py
```

## 🎯 Usage Examples

### Basic Scenario Comparison

1. Open the simulator in your browser
2. Configure three different loan scenarios:
   - **Scenario 1**: €300,000 loan, 25 years, 4.2% rate
   - **Scenario 2**: €250,000 loan, 20 years, 3.8% rate  
   - **Scenario 3**: €400,000 loan, 30 years, 4.8% rate
3. Watch real-time updates across all charts and tables
4. Export detailed amortization schedules as CSV

### Advanced Features

- **Custom insurance rates**: Factor in mortgage insurance costs
- **Down payment impact**: See how different down payments affect total cost
- **Interactive charts**: Click and explore payment breakdowns
- **Responsive design**: Works on desktop, tablet, and mobile

## 🔧 Code Structure

```
loan_simulator.py           # Main Marimo notebook
├── Parameter inputs        # Interactive sliders and forms
├── Calculation engine     # Loan mathematics and amortization
├── Visualization suite    # Multi-panel reactive charts
├── Data export tools      # CSV generation functionality
└── Documentation cells    # Usage guide and examples
```

## 🌟 Why Marimo?

This project showcases advantages over traditional notebook approaches:

| Feature | Jupyter + Streamlit | Marimo |
|---------|-------------------|--------|
| **Development** | Separate notebook + app files | Single .py file |
| **Reactivity** | Manual re-runs + callbacks | Automatic dependency tracking |
| **Deployment** | Complex conversion process | `marimo run` |
| **Version Control** | JSON merge conflicts | Clean Python diffs |
| **State Management** | Hidden state issues | Guaranteed consistency |

## 📈 Performance Benefits

- **Instant updates**: Only affected calculations re-run
- **Memory efficient**: Lazy evaluation for large datasets
- **Parallel execution**: Multi-core processing where possible
- **Production ready**: Built-in error handling and validation

## 🤝 Contributing

We welcome contributions! Here are ways to help:

1. **Report bugs**: Open issues for any problems you encounter
2. **Feature requests**: Suggest new calculator types or improvements
3. **Code contributions**: Submit PRs for new features
4. **Documentation**: Improve examples and explanations

### Development Setup

```bash
# Fork the repository
git clone https://github.com/yourusername/marimo-loan-simulator.git
cd marimo-loan-simulator

# Create development environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install marimo[sql] pytest black

# Make your changes and test
marimo edit loan_simulator.py
```

## 📚 Learn More

- **[Marimo Documentation](https://docs.marimo.io)**: Complete guides and API reference
- **[Marimo Tutorial](https://marimo.io/tutorial)**: Interactive introduction
- **[Examples Gallery](https://marimo.io/gallery)**: More Marimo applications
- **[DataGyver Newsletter](https://glups.uno/HZ3vzW)**: Monthly data science insights

## 🎓 Educational Use

This simulator is perfect for:

- **Teaching financial literacy**: Interactive loan calculations
- **Learning reactive programming**: See dependency graphs in action
- **Demonstrating modern data tools**: Marimo, Plotly, Pandas integration
- **Workshop material**: Hands-on notebook development

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/marimo-loan-simulator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/marimo-loan-simulator/discussions)
- **Marimo Discord**: [Join the community](https://discord.gg/JE7nhX6mD8)

---

**⭐ If this project helps you, please give it a star!**

Built with ❤️ using [Marimo](https://marimo.io) - The next generation of Python notebooks
