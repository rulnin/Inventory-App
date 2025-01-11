#!/usr/bin/env python3
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash_table
from dash.dependencies import Input, Output
import pymysql
import sqlalchemy as sa


engine = sa.create_engine(r"mysql+pymysql://{user}:{pw}@localhost/{db}".format(user="root", pw="230899", db="mango"))

dataset= pd.read_sql(""" SELECT * from mango.stocks_report WHERE DATE(report_date) >= (SELECT max(DATE(report_date))from mango.stocks_report);""",engine)
engine.dispose()   
dataset= dataset.loc[:,['description','size','color','section','subfamily','brand','min',
                        'max','current_stock','total_requested','requested_to_order',
                        'current_stock_value','three_month_revenue','three_month_sales',
                        'three_month_profit','ordered_stock_value','product_mix','drivers','report_date','stock_cost']]
                  
dataset['report_date']= pd.to_datetime(dataset['report_date'])
dataset['three_month_cogs']= dataset['stock_cost']* dataset['three_month_sales']
all_subfamily= dataset.subfamily.unique()
all_section= dataset.section.unique()
all_brand= dataset.brand.unique()
all_items= dataset.description.unique()
all_drivers= dataset.drivers.unique()
all_abc= dataset.product_mix.unique()

app= dash.Dash(__name__)
app.layout= html.Div([
    html.H1('Inventory App',
        style={
            'fontSize': '48px',  # Set the font size
            'textAlign': 'center'  # Center-align the text
        }),
    html.Br(),
    html.H6('Choose Subfamily',
            style={
            'fontSize': '15px',  # Set the font size
            }),
    dcc.Dropdown(id= 'subfamily',
                 options= [{'label':i,'value':i} for i in all_subfamily]+ [{'label':'ALL','value':'All'}],
                 value='All',
                 multi=True),
    html.H6('Choose brand',
            style={
            'fontSize': '15px',  # Set the font size
            }),
    dcc.Dropdown(id= 'brand',
                 options= [{'label':i,'value':i} for i in all_brand]+ [{'label':'ALL','value':'All'}],
                 value='All',
                 multi=True),
    html.H6('Choose section',
            style={
            'fontSize': '15px',  # Set the font size
            }),
    dcc.Dropdown(id= 'section',
                 options= [{'label':i,'value':i} for i in all_section]+ [{'label':'ALL','value':'All'}],
                 value='All',
                 multi=True),
    html.H6('Choose drivers',
            style={
            'fontSize': '15px',  # Set the font size
            }),
    dcc.Dropdown(id= 'drivers',
                 options= [{'label':i,'value':i} for i in all_drivers]+ [{'label':'ALL','value':'All'}],
                 value='All',
                 multi=True),
    html.H6('Choose category',
            style={
            'fontSize': '15px',  # Set the font size
            }),
    dcc.Dropdown(id= 'abc',
                 options= [{'label':i,'value':i} for i in all_abc]+ [{'label':'ALL','value':'All'}],
                 value='All',
                 multi=True),
    html.H6('Choose descritpion',
            style={
            'fontSize': '15px',  # Set the font size
            }),
    dcc.Dropdown(id= 'description',
                 options= [{'label':i,'value':i} for i in all_items]+ [{'label':'ALL','value':'All'}],
                 value='All',
                 multi=True),
    html.Div(children= 'Business Overview',
        style={
            'fontSize': '25px',  # Set the font size
            'textAlign': 'center',  # Center-align the text
            'marginTop': '90px',  # Add top margin to increase spacing
            'fontWeight': 'bold'  # Make the font bold
        }),
    dcc.Graph(id= 'Bar'),
    # html.Div(children= 'Category Overview',
    #     style={
    #         'fontSize': '25px',  # Set the font size
    #         'textAlign': 'center',  # Center-align the text
    #         'fontWeight': 'bold'  # Make the font bold
    #     }),
    dcc.Graph(id= 'pie',
        style={
            'width': '90%',  # Set the width of the graph
            'height': '800px'  # Set the height of the graph
        }),
    html.Br(),
    html.H6('select attribute for ranking',
            style={
            'fontSize': '15px',  # Set the font size
            }),
    html.Div(dcc.Dropdown(id= 'ranking_att',value='subfamily',
                          clearable= False,options= [{'label': x,'value':x} for x in ['subfamily',
                                                                                      'description',
                                                                                      'drivers',
                                                                                      'section',
                                                                                      'brand',
                                                                                      'product_mix']]),
             className= 'six columns'),
    html.H6('select value for ranking',
            style={
            'fontSize': '15px',  # Set the font size
            }),
    html.Div(dcc.Dropdown(id= 'value_att',value='three_month_sales',
                          clearable= False,options= [{'label': x,'value':x} for x in ['three_month_sales',
                                                                                      'three_month_revenue',
                                                                                      'three_month_cogs',
                                                                                      'three_month_profit',
                                                                                      'current_stock_value',
                                                                                      'ordered_stock_value']]),
             className= 'six columns'),
    dcc.Graph(id= 'top'),
    html.Div(children= 'Ranking Data',
        style={
            'fontSize': '25px',  # Set the font size
            'textAlign': 'center',  # Center-align the text
            'fontWeight': 'bold'  # Make the font bold
        }),
    dash_table.DataTable(id= 'table_ranking',
                         editable = True,
                         filter_action= 'native',
                         sort_action= 'native',
                         sort_mode= 'single',
                         column_selectable= 'multi',
                         selected_columns= [],
                         selected_rows= [],
                         page_action= 'native',
                         page_current=0,
                         page_size= 6,
                         export_format='csv',
                         style_cell = { 'minWidth':95, 'maxWidth':95,'Width':95},
                         style_data= { 'whiteSpace': 'normal','height': 'auto'}),
    html.Div(children= 'Filtered Data',
        style={
            'fontSize': '25px',  # Set the font size
            'textAlign': 'center',  # Center-align the text
            'fontWeight': 'bold'  # Make the font bold
        }),
    dash_table.DataTable(id= 'filtered',
                         columns= [{'name': i,'id':i,'deletable':True,'selectable':True,'hideable':True}for i in
                                   dataset.columns],
                         editable = True,
                         filter_action= 'native',
                         sort_action= 'native',
                         sort_mode= 'single',
                         column_selectable= 'multi',
                         selected_columns= [],
                         selected_rows= [],
                         page_action= 'native',
                         page_current=0,
                         page_size= 6,
                         export_format='csv',
                         style_cell = { 'minWidth':95, 'maxWidth':95,'Width':95},
                         style_data= { 'whiteSpace': 'normal','height': 'auto'}),
    html.Br(),
    html.H6('Red- Alarm: important drivers that neeeds to b replinished immediatley-Zero stocks',
        style={
            'fontSize': '25px',  # Set the font size
            'textAlign': 'center'  # Center-align the text
        }),
    dash_table.DataTable(id= 'red_alarm',
                         columns= [{'name': i,'id':i,'deletable':True,'selectable':True,'hideable':True}for i in
                                   dataset.columns],
                         editable = True,
                         filter_action= 'native',
                         sort_action= 'native',
                         sort_mode= 'single',
                         column_selectable= 'multi',
                         selected_columns= [],
                         selected_rows= [],
                         page_action= 'native',
                         page_current=0,
                         page_size= 6,
                         export_format='csv',
                         style_cell = { 'minWidth':95, 'maxWidth':95,'Width':95},
                         style_data= { 'whiteSpace': 'normal','height': 'auto'}),
    html.Br(),
    html.H6('Orange- Alarm: important drivers that neeeds to b replinished immediatley-Below Minimum',
        style={
            'fontSize': '25px',  # Set the font size
            'textAlign': 'center'  # Center-align the text
        }),
    dash_table.DataTable(id= 'orange_alarm',
                         columns= [{'name': i,'id':i,'deletable':True,'selectable':True,'hideable':True}for i in
                                   dataset.columns],
                         editable = True,
                         filter_action= 'native',
                         sort_action= 'native',
                         sort_mode= 'single',
                         column_selectable= 'multi',
                         selected_columns= [],
                         selected_rows= [],
                         page_action= 'native',
                         page_current=0,
                         page_size= 6,
                         export_format='csv',
                         style_cell = { 'minWidth':95, 'maxWidth':95,'Width':95},
                         style_data= { 'whiteSpace': 'normal','height': 'auto'})
    
    ])
@app.callback([Output('table_ranking', 'columns'),
               Output('table_ranking', 'data'),
               Output('filtered', 'data'),
               Output('Bar', 'figure'),
               Output('pie', 'figure'),
               Output('top', 'figure'),
               Output('red_alarm', 'data'),
               Output('orange_alarm', 'data'),
               Output('red_alarm', 'row_deletable'),
               Output('orange_alarm', 'row_deletable'),
               Output('table_ranking', 'row_deletable'),
               Output('filtered', 'row_deletable')],
              [Input('subfamily','value'),
               Input('brand','value'),
               Input('section','value'),
               Input('description','value'),
               Input('drivers','value'),
               Input('value_att','value'),
               Input('ranking_att','value'),
               Input('abc','value')
               
                  ])
def update_table(sub,bran,sec,desc,driv,val_d,rank_att,ab):
    data= dataset
    if 'All' in sub:
        data= data.loc[data['subfamily'] != 'All',:]
    else:
        data= data.loc[data['subfamily'].isin(sub),:]
    if 'All' in bran:
        data= data.loc[data['brand'] != 'All',:]
    else:
        data= data.loc[data['brand'].isin(bran),:]
    if 'All' in sec:
        data= data.loc[data['section'] != 'All',:]
    else:
        data= data.loc[data['section'].isin(sec),:]
    if 'All' in desc:
        data= data.loc[data['description'] != 'All',:]
    else:
        data= data.loc[data['description'].isin(desc),:]
    if 'All' in driv:
        data= data.loc[data['drivers'] != 'All',:]
    else:
        data= data.loc[data['drivers'].isin(driv),:]
    if 'All' in ab:
        data= data.loc[data['product_mix'] != 'All',:]
    else:
        data= data.loc[data['product_mix'].isin(ab),:]
        
        
    ranking_data= data.groupby(rank_att).agg(three_month_revenue= ('three_month_revenue','sum'),
                                             three_month_sales= ('three_month_sales','sum'),
                                             three_month_cogs= ('three_month_cogs','sum'),
                                             three_month_profit= ('three_month_profit','sum'),
                                             current_stock_value= ('current_stock_value','sum'),
                                             ordered_stock_value= ('ordered_stock_value','sum'),
                                             requested_to_order= ('requested_to_order','sum')
                                             
        ).sort_values(by=val_d,ascending=False).reset_index()
    ranking_data['inventory_turns']= ranking_data['three_month_cogs']/ranking_data['current_stock_value']
    ranking_data['margin']= 1- (ranking_data['three_month_cogs']/ranking_data['three_month_revenue'])

    ranking_columns= [{'name': i,'id':i,'deletable':True,'selectable':True,'hideable':True}for i in
                                   ranking_data.columns]

    important_drivers= ['Volume and margin driver','Volume driver','Margin driver']
    red_alarm= data.loc[(data.drivers.isin(important_drivers)) & (data['current_stock']==0),:]
    red_alarm= red_alarm.loc[(red_alarm['total_requested']==0) & (red_alarm['min']>0),:]
    
    orange_alarm= data.loc[(data.drivers.isin(important_drivers)) & (data['min']>0),:]
    orange_alarm= orange_alarm.loc[(orange_alarm['total_requested'] +orange_alarm['current_stock'] ) <= orange_alarm['min'],:]
    specs= [[{'type': 'domain'},{'type': 'domain'}],[{'type': 'domain'},{'type': 'domain'}]]
    pie_fig= make_subplots(rows=2,cols=2 ,specs= specs)
    pie_fig.add_trace(go.Pie(labels= data['product_mix'],values= data['three_month_revenue'],
                             name= 'Three Month Rvenue',title= 'Three Month Revenue'),1,1
        )
    pie_fig.add_trace(go.Pie(labels= data['product_mix'],values= data['three_month_sales'],
                             name= 'Three Month sales',title= 'Three Month sales'),1,2
        )
    pie_fig.add_trace(go.Pie(labels= data['product_mix'],values= data['current_stock_value'],
                             name= 'current_stock_value',title= 'current_stock_value'),2,1
        )
    pie_fig.add_trace(go.Pie(labels= data['product_mix'],values= data['ordered_stock_value'],
                             name= 'ordered_stock_value',title= 'ordered_stock_value'),2,2
        )

    pie_fig.update_traces(hoverinfo= 'label+percent',textinfo='none')
    pie_fig.update(layout_title_text= 'Category Overview',layout_showlegend=True)
    pie_fig= go.Figure(pie_fig)
    
    top_fig= px.bar(ranking_data.iloc[0:15,:],x= val_d,y= rank_att)
    
    
    for_bar= data.groupby('section').agg(three_month_revenue= ('three_month_revenue','sum'),
                                             three_month_cogs= ('three_month_cogs','sum'),
                                             current_stock_value= ('current_stock_value','sum'),
                                             ordered_stock_value= ('ordered_stock_value','sum')
                                             
        ).reset_index()
    bar_fig= go.Figure(data=[
        go.Bar(name= 'three_month_revenue',x= for_bar['section'],y= for_bar['three_month_revenue']),
        go.Bar(name= 'three_month_cogs',x= for_bar['section'],y= for_bar['three_month_cogs']),
        go.Bar(name= 'current_stock_value',x= for_bar['section'],y= for_bar['current_stock_value']),
        go.Bar(name= 'ordered_stock_value',x= for_bar['section'],y= for_bar['ordered_stock_value'])]).update_layout(barmode='group')

        

    return [ranking_columns,
           ranking_data.to_dict('records'),
           data.to_dict('records'),
           bar_fig,
           pie_fig,
           top_fig,
           red_alarm.to_dict('records'),
           orange_alarm.to_dict('records'),True,True,True,True]

if __name__== '__main__':
    app.run_server(debug=True)







