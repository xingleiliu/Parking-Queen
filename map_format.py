
import pandas as pd
import folium
import branca
import numpy as np



def add_legends_popup(dataframe, m, lan, long):

    # pin user input location on the map
    folium.Marker(
        location=[lan, long],
        icon=folium.Icon(color= 'cadetblue', popup='My Destination', prefix='fa', icon='circle')
    ).add_to(m)
    
    lgd_txt = '<span style="color: {col};">{txt}</span>'
    price_list = ['less or equal to $1', 'between $1 and $2', 'between $2 and $3', 'greater than $3']
    color = ['green', 'blue', 'orange', 'red']

    for idx in range(len(price_list)): 

        fg = folium.FeatureGroup(name= lgd_txt.format( txt= 'Lowest Rate: '+ price_list[idx] , col= color[idx]))

        m.add_child(fg)

    for i in range(0,len(dataframe)):
        LowestRate = dataframe['LowestRate'].iloc[i]
        if LowestRate <= np.float(1.0):
            color = 'green'
        elif LowestRate > np.float(1.0) and LowestRate <= np.float(2.0):
            color = 'blue'
        elif LowestRate > np.float(2.0) and LowestRate <= np.float(3.0):
            color = 'orange'
        else:
            color = 'red'

        html = popup_html(i, dataframe)
        iframe = branca.element.IFrame(html=html,width=510,height=280)
        popup = folium.Popup(folium.Html(html, script=True), max_width=500)


        folium.Marker([dataframe['Lan'].iloc[i],dataframe['Long'].iloc[i]],popup=popup,
                     icon=folium.Icon(color=color, prefix='fa', icon = 'car')).add_to(m)

    folium.map.LayerControl('bottomleft', collapsed= False).add_to(m)

    
    return m 






def popup_html(row, dataframe):
    
    i = row
    BlockFace=dataframe['BlockFace'].iloc[i] 
    MeterType=dataframe['MeterType'].iloc[i]
    RateType = dataframe['RateType'].iloc[i] 
    RateRange=dataframe['RateRange'].iloc[i] 
    MeteredTimeLimit = dataframe['MeteredTimeLimit'].iloc[i]                      
    ParkingPolicy = dataframe['ParkingPolicy'].iloc[i]

    left_col_color = "#B4CFB0"
    right_col_color = "#F1E0AC"
    
    html = """<!DOCTYPE html>
<html>

<head>
<h4 style="margin-bottom:10"; width="200px">{}</h4>""".format(BlockFace) + """

</head>
    <table style="height: 126px; width: 350px;">
<tbody>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Meter Type</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(MeterType) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Rate Type</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(RateType) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Rate Range</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(RateRange) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Metered Time Limit</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(MeteredTimeLimit) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Parking Policy</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(ParkingPolicy) + """
</tr>
</tbody>
</table>
</html>
"""
    return html















