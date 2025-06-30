"""
Simulateur de Prêt Multi-Scénarios avec Marimo
============================================

Installation : pip install marimo pandas plotly
Lancement : marimo edit marimo_loan_simulator.py
Déploiement : marimo run marimo_loan_simulator.py
"""

import marimo

__generated_with = "0.14.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    import numpy as np
    return go, make_subplots, mo, np, pd, px


@app.cell
def _(mo):
    mo.md(
        r"""
        # 🏠 Simulateur de Prêt - Analyse des Scénarios

        **Comparez l'impact du budget, de la durée, du taux et de l'apport sur votre financement**

        Configurez votre budget immobilier et explorez 3 stratégies :  
        - **Scénario 1** : Votre configuration de référence  
        - **Scénario 2** : Impact d'un apport plus important  
        - **Scénario 3** : Impact d'une durée et/ou taux différent  
        
        *Adaptable à tous budgets : studio étudiant, maison familiale, ou investissement locatif*
        """
    )
    return


@app.cell
def _(mo):
    mo.md("## 🏡 Configuration de votre Projet")
    return


@app.cell
def _(mo):
    project_price = mo.ui.slider(
        start=100000, 
        stop=1500000, 
        value=350000, 
        step=10000, 
        label="Prix du bien immobilier (€)"
    )
    project_price
    return (project_price,)


@app.cell
def _(mo, project_price):
    # Suggestions contextuelles selon le budget
    if project_price.value <= 200000:
        suggestion = "💡 **Budget studio/T2** : Idéal pour primo-accédant ou investissement locatif"
    elif project_price.value <= 400000:
        suggestion = "💡 **Budget maison/grand appartement** : Parfait pour résidence principale familiale"
    elif project_price.value <= 800000:
        suggestion = "💡 **Budget premium** : Bien de standing ou grande propriété"
    else:
        suggestion = "💡 **Budget luxury/investissement** : Propriété haut de gamme ou portefeuille locatif"
    
    mo.md(f"""
    {suggestion}
    
    **Exemples de stratégies selon votre profil :**  
    - **Primo-accédant** : Minimiser l'apport, maximiser les aides (PTZ, etc.)  
    - **Famille** : Équilibrer mensualité et durée selon revenus  
    - **Investisseur** : Optimiser la fiscalité et la rentabilité  
    """)
    return (suggestion,)


@app.cell
def _(mo):
    base_insurance_rate = mo.ui.slider(
        start=0.0, 
        stop=1.0, 
        value=0.36, 
        step=0.01, 
        label="Taux d'assurance emprunteur (%)"
    )
    base_insurance_rate
    return (base_insurance_rate,)


@app.cell
def _(mo):
    mo.md("## 📊 Scénario 1 - Configuration de Référence")
    return


@app.cell
def _(mo, project_price):
    # Apport suggéré : entre 10% et 30% du prix
    suggested_min_down = int(project_price.value * 0.10)
    suggested_max_down = int(project_price.value * 0.40)
    suggested_down = int(project_price.value * 0.15)  # 15% par défaut
    
    s1_down_payment = mo.ui.slider(
        start=suggested_min_down, 
        stop=suggested_max_down, 
        value=min(suggested_down, suggested_max_down), 
        step=5000, 
        label=f"Apport personnel (€) - Suggéré : {suggested_down/project_price.value*100:.0f}% du prix"
    )
    s1_down_payment
    return (s1_down_payment, suggested_down, suggested_max_down, suggested_min_down)


@app.cell
def _(mo):
    s1_rate = mo.ui.slider(
        start=1.0, 
        stop=8.0, 
        value=4.2, 
        step=0.1, 
        label="Taux d'intérêt (%)"
    )
    s1_rate
    return (s1_rate,)


@app.cell
def _(mo):
    s1_years = mo.ui.dropdown(
        options=[15, 20, 25, 30], 
        value=25, 
        label="Durée (années)"
    )
    s1_years
    return (s1_years,)


@app.cell
def _(mo):
    mo.md("## 📈 Scénario 2 - Impact Apport Supplémentaire")
    return


@app.cell
def _(mo, project_price):
    # Apport supplémentaire : jusqu'à 15% du prix du bien
    max_additional = int(project_price.value * 0.15)
    default_additional = min(30000, max_additional // 2)
    
    s2_additional_down = mo.ui.slider(
        start=0, 
        stop=max_additional, 
        value=default_additional, 
        step=5000, 
        label=f"Apport supplémentaire (€) - Max suggéré : {max_additional:,.0f} €"
    )
    s2_additional_down
    return (default_additional, max_additional, s2_additional_down)


@app.cell
def _(mo):
    mo.md("## 🚀 Scénario 3 - Impact Durée/Taux Différent")
    return


@app.cell
def _(mo):
    s3_rate = mo.ui.slider(
        start=1.0, 
        stop=8.0, 
        value=3.8, 
        step=0.1, 
        label="Taux d'intérêt alternatif (%)"
    )
    s3_rate
    return (s3_rate,)


@app.cell
def _(mo):
    s3_years = mo.ui.dropdown(
        options=[15, 20, 25, 30], 
        value=20, 
        label="Durée alternative (années)"
    )
    s3_years
    return (s3_years,)


@app.cell
def _(project_price, s1_down_payment, s1_rate, s1_years, base_insurance_rate,
      s2_additional_down, s3_rate, s3_years):
    
    # Fonction de calcul des prêts
    def calculate_loan_scenario(project_price, down_payment, rate, years, insurance_rate):
        """Calcule tous les détails d'un scénario de prêt"""
        loan_amount = project_price - down_payment
        monthly_rate = rate / 100 / 12
        n_payments = years * 12
        insurance_monthly = loan_amount * insurance_rate / 100 / 12

        if monthly_rate > 0:
            monthly_payment = (loan_amount * monthly_rate * (1 + monthly_rate)**n_payments) / \
                            ((1 + monthly_rate)**n_payments - 1)
        else:
            monthly_payment = loan_amount / n_payments

        monthly_payment_total = monthly_payment + insurance_monthly
        total_cost = monthly_payment_total * n_payments
        total_interest = total_cost - loan_amount

        return {
            'loan_amount': loan_amount,
            'down_payment': down_payment,
            'monthly_payment': round(monthly_payment, 0),
            'monthly_insurance': round(insurance_monthly, 0),
            'monthly_payment_total': round(monthly_payment_total, 0),
            'total_cost': round(total_cost, 0),
            'total_interest': round(total_interest, 0),
            'monthly_rate': monthly_rate,
            'n_payments': n_payments,
            'rate': rate,
            'years': years
        }

    # Calcul des 3 scénarios
    scenario1 = calculate_loan_scenario(
        project_price.value, s1_down_payment.value, s1_rate.value, 
        s1_years.value, base_insurance_rate.value
    )

    scenario2 = calculate_loan_scenario(
        project_price.value, s1_down_payment.value + s2_additional_down.value, 
        s1_rate.value, s1_years.value, base_insurance_rate.value
    )

    scenario3 = calculate_loan_scenario(
        project_price.value, s1_down_payment.value, s3_rate.value, 
        s3_years.value, base_insurance_rate.value
    )

    return (calculate_loan_scenario, scenario1, scenario2, scenario3)


@app.cell
def _(mo, scenario1, scenario2, scenario3, project_price):
    
    # Calculs de ratios utiles
    monthly_to_income_30 = scenario1['monthly_payment_total'] / 0.30  # Revenu nécessaire pour 30% d'endettement
    monthly_to_income_33 = scenario1['monthly_payment_total'] / 0.33  # Revenu nécessaire pour 33% d'endettement
    
    # Résumé des scénarios configurés
    mo.md(f"""
    ## 📋 Résumé de votre Projet Immobilier
    
    **🏡 Bien immobilier :** {project_price.value:,.0f} € 
    **💰 Revenus nécessaires :** {monthly_to_income_30:,.0f} € nets/mois (30% endettement) | {monthly_to_income_33:,.0f} € nets/mois (33% endettement)
    
    | Scénario | Apport | Emprunt | Taux | Durée | Mensualité | Assurance | **Total/mois** | Coût total |
    |----------|--------|---------|------|-------|------------|-----------|----------------|------------|
    | **Référence** | {scenario1['down_payment']:,.0f} € | {scenario1['loan_amount']:,.0f} € | {scenario1['rate']:.1f}% | {scenario1['years']} ans | {scenario1['monthly_payment']:,.0f} € | {scenario1['monthly_insurance']:,.0f} € | **{scenario1['monthly_payment_total']:,.0f} €** | {scenario1['total_cost']:,.0f} € |
    | **+ Apport** | {scenario2['down_payment']:,.0f} € | {scenario2['loan_amount']:,.0f} € | {scenario2['rate']:.1f}% | {scenario2['years']} ans | {scenario2['monthly_payment']:,.0f} € | {scenario2['monthly_insurance']:,.0f} € | **{scenario2['monthly_payment_total']:,.0f} €** | {scenario2['total_cost']:,.0f} € |
    | **Durée/Taux** | {scenario3['down_payment']:,.0f} € | {scenario3['loan_amount']:,.0f} € | {scenario3['rate']:.1f}% | {scenario3['years']} ans | {scenario3['monthly_payment']:,.0f} € | {scenario3['monthly_insurance']:,.0f} € | **{scenario3['monthly_payment_total']:,.0f} €** | {scenario3['total_cost']:,.0f} € |
    """)
    return (monthly_to_income_30, monthly_to_income_33)


@app.cell
def _(scenario1, scenario2, scenario3):
    # Calcul des économies/surcoûts
    ref_monthly = scenario1['monthly_payment_total']
    ref_total = scenario1['total_cost']
    
    # Économies scénario 2 (+ apport)
    s2_monthly_saving = ref_monthly - scenario2['monthly_payment_total']
    s2_total_saving = ref_total - scenario2['total_cost']
    
    # Économies scénario 3 (durée/taux)
    s3_monthly_diff = scenario3['monthly_payment_total'] - ref_monthly
    s3_total_diff = scenario3['total_cost'] - ref_total
    
    return (ref_monthly, ref_total, s2_monthly_saving, s2_total_saving, s3_monthly_diff, s3_total_diff)


@app.cell
def _(mo, s2_monthly_saving, s2_total_saving, s3_monthly_diff, s3_total_diff, s2_additional_down):
    
    # Analyse des économies
    mo.md(f"""
    ## 💰 Analyse des Économies
    
    ### 📈 Impact de l'apport supplémentaire (+{s2_additional_down.value:,.0f} €)
    - **Économie mensuelle :** {s2_monthly_saving:+.0f} €/mois
    - **Économie totale :** {s2_total_saving:+.0f} €
    - **Retour sur investissement :** {s2_total_saving/s2_additional_down.value*100 if s2_additional_down.value > 0 else 0:.1f}% sur la durée du prêt
    
    ### 🚀 Impact durée/taux différent
    - **Différence mensuelle :** {s3_monthly_diff:+.0f} €/mois
    - **Différence totale :** {s3_total_diff:+.0f} €
    - **{"📉 Économie" if s3_total_diff < 0 else "📈 Surcoût"}** de {abs(s3_total_diff):,.0f} € au total
    """)
    return


@app.cell
def _(go, scenario1, scenario2, scenario3):
    
    # Graphique de comparaison des mensualités
    fig_monthly = go.Figure()
    
    scenarios = ['Référence', '+ Apport', 'Durée/Taux']
    monthly_totals = [scenario1['monthly_payment_total'], 
                     scenario2['monthly_payment_total'], 
                     scenario3['monthly_payment_total']]
    monthly_capital = [scenario1['monthly_payment'], 
                      scenario2['monthly_payment'], 
                      scenario3['monthly_payment']]
    monthly_insurance = [scenario1['monthly_insurance'], 
                        scenario2['monthly_insurance'], 
                        scenario3['monthly_insurance']]
    
    colors = ['#3498db', '#2ecc71', '#e74c3c']
    
    # Mensualité capital
    fig_monthly.add_trace(go.Bar(
        name='Capital + Intérêts',
        x=scenarios,
        y=monthly_capital,
        marker_color=colors,
        text=[f"{mp:,.0f} €" for mp in monthly_capital],
        textposition='inside'
    ))
    
    # Assurance
    fig_monthly.add_trace(go.Bar(
        name='Assurance',
        x=scenarios,
        y=monthly_insurance,
        marker_color=['lightblue', 'lightgreen', 'lightcoral'],
        text=[f"{mi:,.0f} €" for mi in monthly_insurance],
        textposition='inside'
    ))
    
    fig_monthly.update_layout(
        title="Comparaison des Mensualités",
        xaxis_title="Scénarios",
        yaxis_title="Mensualité (€)",
        barmode='stack',
        height=400
    )
    
    fig_monthly
    return (colors, fig_monthly, monthly_capital, monthly_insurance, monthly_totals, scenarios)


@app.cell
def _(go, make_subplots, scenario1, scenario2, scenario3):
    
    # Graphique double : Coût total vs Économies
    fig_costs = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Coût Total du Crédit', 'Économies Potentielles'),
        specs=[[{"type": "bar"}, {"type": "bar"}]]
    )
    
    # Coût total
    total_costs = [scenario1['total_cost']/1000, scenario2['total_cost']/1000, scenario3['total_cost']/1000]
    fig_costs.add_trace(
        go.Bar(x=['Référence', '+ Apport', 'Durée/Taux'], 
               y=total_costs,
               marker_color=['#3498db', '#2ecc71', '#e74c3c'],
               text=[f"{cost:.0f} K€" for cost in total_costs],
               textposition='auto',
               name='Coût Total'),
        row=1, col=1
    )
    
    # Économies (par rapport à la référence)
    savings = [0, (scenario1['total_cost'] - scenario2['total_cost'])/1000, 
               (scenario1['total_cost'] - scenario3['total_cost'])/1000]
    colors_savings = ['gray', 'green' if savings[1] > 0 else 'red', 
                     'green' if savings[2] > 0 else 'red']
    
    fig_costs.add_trace(
        go.Bar(x=['Référence', '+ Apport', 'Durée/Taux'], 
               y=savings,
               marker_color=colors_savings,
               text=[f"{s:+.0f} K€" if s != 0 else "Ref." for s in savings],
               textposition='auto',
               name='Économies'),
        row=1, col=2
    )
    
    fig_costs.update_layout(
        height=400,
        showlegend=False
    )
    
    fig_costs.update_yaxes(title_text="Coût (K€)", row=1, col=1)
    fig_costs.update_yaxes(title_text="Économies (K€)", row=1, col=2)
    
    fig_costs
    return (colors_savings, fig_costs, savings, total_costs)


@app.cell
def _(go, scenario1, scenario2, scenario3):
    
    # Évolution du capital restant dû pour les 3 scénarios
    def generate_schedule_comparison(scenario, name):
        """Génère l'évolution du capital pour un scénario"""
        schedule = []
        remaining = scenario['loan_amount']
        
        for month in range(1, int(scenario['n_payments']) + 1):
            interest = remaining * scenario['monthly_rate']
            principal = scenario['monthly_payment'] - interest
            remaining -= principal
            
            schedule.append({
                'month': month,
                'remaining': max(0, remaining),
                'scenario': name
            })
            
            if remaining <= 0:
                break
        
        return schedule
    
    # Génération des données
    schedule_ref = generate_schedule_comparison(scenario1, 'Référence')
    schedule_apport = generate_schedule_comparison(scenario2, '+ Apport') 
    schedule_alt = generate_schedule_comparison(scenario3, 'Durée/Taux')
    
    fig_evolution = go.Figure()
    
    schedules_data = [
        (schedule_ref, '#3498db', 'Référence'),
        (schedule_apport, '#2ecc71', '+ Apport'),
        (schedule_alt, '#e74c3c', 'Durée/Taux')
    ]
    
    for schedule, color, name in schedules_data:
        months = [s['month'] for s in schedule]
        remaining = [s['remaining'] for s in schedule]
        
        fig_evolution.add_trace(go.Scatter(
            x=months,
            y=remaining,
            mode='lines',
            name=name,
            line=dict(color=color, width=3)
        ))
    
    fig_evolution.update_layout(
        title="Évolution du Capital Restant Dû",
        xaxis_title="Mois",
        yaxis_title="Capital restant (€)",
        height=500,
        hovermode='x unified'
    )
    
    fig_evolution
    return (fig_evolution, generate_schedule_comparison, schedule_alt, schedule_apport, schedule_ref, schedules_data)


@app.cell
def _(mo):
    # Section d'aide
    mo.md(
        r"""
        ---

        ## ℹ️ Guide d'Utilisation

        ### 🎯 Logique du Simulateur
        - **Adaptable à tous budgets** : Studio à 150K€ ou villa à 800K€
        - **3 stratégies financières** : Comparez l'impact de vos choix
        - **Réactivité totale** : Chaque modification met à jour tous les calculs

        ### 🏠 Exemples par Budget
        
        **🏠 Budget 150-250K€** *(Studio, T2, primo-accédant)*
        - Apport minimum : 15-30K€ (10-15%)
        - Focus : Minimiser mensualité, maximiser aides publiques
        - Durée : 25-30 ans pour réduire les mensualités
        
        **🏠 Budget 250-450K€** *(T3-T4, maison familiale)*
        - Apport standard : 40-80K€ (15-20%)
        - Focus : Équilibrer mensualité et coût total
        - Durée : 20-25 ans selon capacité de remboursement
        
        **🏠 Budget 450K€+** *(Maison premium, investissement)*
        - Apport important : 90K€+ (20%+)
        - Focus : Optimisation fiscale et rentabilité
        - Durée : Variable selon stratégie patrimoniale

        ### 📊 Scénarios Comparés
        1. **Référence** : Votre configuration de base
        2. **+ Apport** : Impact d'un apport supplémentaire (même taux/durée)  
        3. **Durée/Taux** : Impact de conditions différentes (même apport)

        ### 💡 Points d'Attention Universels
        - **Apport supplémentaire** : ROI vs autres placements
        - **Durée plus courte** : Mensualité élevée mais économies importantes
        - **Négociation taux** : 0.1% = plusieurs milliers d'euros d'économie
        - **Ratio d'endettement** : 30-33% max de vos revenus nets

        ### 🚀 Cas d'Usage Pratiques
        - **Négociation banque** : "Si vous me faites 0.2% de moins..."
        - **Décision apport** : "Est-ce que je vide mon livret A ?"
        - **Choix durée** : "20 ans ou 25 ans ?"
        - **Comparaison biens** : Impact budget sur faisabilité

        ---

        **💡 Développé avec Marimo** - Réactivité au service de tous vos projets immobiliers  
        **🔗 Code source** : [marimo-loan-simulator](https://github.com/yourusername/marimo-loan-simulator)
        """
    )
    return


if __name__ == "__main__":
    app.run()