# 🏠 Marimo Loan Simulator

Interactive loan simulator built with Marimo - multi-scenario comparison with reactive charts and instant web app deployment

[![Marimo](https://img.shields.io/badge/Built%20with-Marimo-blue)](https://marimo.io)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-brightgreen)](https://gpenessot.github.io/marimo-loan-simulator/)

## 🚀 Features

- **Universal budget compatibility**: From 100K€ studio to 1.5M€ luxury property
- **Smart scenario comparison**: Reference vs additional down payment vs different rate/duration
- **Intelligent suggestions**: Automatic down payment recommendations based on property price
- **Real-time calculations**: Monthly payments, insurance, total cost, and income requirements
- **Professional visualizations**: Evolution charts, cost comparisons, ROI analysis
- **Instant deployment**: Transform notebook to web app with one command
- **Git-friendly storage**: Pure Python files, no JSON conflicts

## 📊 What You'll Discover

This simulator demonstrates real-world financial decision-making:

- **Budget impact analysis**: How property price affects financing options
- **Down payment ROI**: When is additional down payment profitable?
- **Rate negotiation value**: Quantify the impact of 0.1% rate difference
- **Duration trade-offs**: Balance monthly payments vs total cost
- **Income requirements**: Automatic calculation for 30% and 33% debt ratios

## 🛠️ Quick Start

### Prerequisites

- Python 3.8+
- pip or conda

### Installation

```bash
# Install Marimo with all dependencies
pip install marimo pandas plotly numpy

# Clone this repository
git clone https://github.com/gpenessot/marimo-loan-simulator.git
cd marimo-loan-simulator
```

### Running the Simulator

**🌐 Live Demo:** [Try it online](https://gpenessot.github.io/marimo-loan-simulator/) (no installation required!)

**As Interactive Notebook:**
```bash
marimo edit marimo_loan_simulator.py
```

**As Web Application:**
```bash
marimo run marimo_loan_simulator.py
```

**As Python Script:**
```bash
python marimo_loan_simulator.py
```

## 🎯 Usage Examples

### Universal Budget Scenarios

**🏠 First-time buyer (150K€ studio):**
- Property: €150,000
- Down payment: €22,500 (15%)
- Compare: 20 vs 25 years duration impact

**🏠 Family home (350K€):**
- Property: €350,000  
- Down payment: €52,500 (15%)
- Compare: Extra €30K down payment ROI vs different rates

**🏠 Investment property (600K€):**
- Property: €600,000
- Down payment: €120,000 (20%)
- Compare: Tax optimization through duration and down payment strategies

### Key Decision Points

- **Down payment optimization**: See immediate impact on monthly payments and total cost
- **Rate negotiation value**: Quantify how 0.2% rate reduction saves thousands
- **Duration strategy**: Balance cash flow (monthly) vs total cost
- **Income planning**: Know exactly what salary you need for each scenario

## 🔧 Code Structure

```
marimo_loan_simulator.py       # Main Marimo notebook
├── Parameter inputs           # Interactive sliders and forms
├── Calculation engine         # Loan mathematics and amortization
├── Visualization suite        # Multi-panel reactive charts
├── Data export tools          # CSV generation functionality
└── Documentation cells       # Usage guide and examples
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
marimo edit marimo_loan_simulator.py
```

## 📚 Learn More

- **[Live Demo](https://gpenessot.github.io/marimo-loan-simulator/)**: Try the simulator online
- **[Marimo Documentation](https://docs.marimo.io)**: Complete guides and API reference
- **[Marimo Tutorial](https://marimo.io/tutorial)**: Interactive introduction
- **[DataGyver Newsletter](https://datagyver.substack.com/)**: Monthly data science insights and tools

## 🎓 Educational Use

Perfect for understanding:

- **Financial literacy**: Interactive loan calculations and comparisons
- **Reactive programming**: See dependency graphs in action with Marimo
- **Modern data tools**: Integration of Marimo, Plotly, and Pandas
- **Real estate finance**: Down payment strategies, rate impacts, duration trade-offs

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[Marimo Team](https://marimo.io)**: For building an incredible reactive notebook platform
- **[DataGyver Community](https://datagyver.substack.com/)**: For inspiration and practical data science insights
- **Contributors**: Everyone who helps improve this financial education tool

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/gpenessot/marimo-loan-simulator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/gpenessot/marimo-loan-simulator/discussions)
- **Marimo Discord**: [Join the community](https://discord.gg/JE7nhX6mD8)

---

**⭐ If this tool helps with your real estate decisions, please give it a star!**

Built with ❤️ using [Marimo](https://marimo.io) - Making financial decisions more transparent and informed