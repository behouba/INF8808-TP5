'''
    Contains the functions to set up the map visualization.

'''

import plotly.graph_objects as go
import plotly.express as px

import hover_template as hover


def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    '''
        Adds the choropleth trace, representing Montreal's neighborhoods.

        Note: The z values and colorscale provided ensure every neighborhood
        will be grey in color. Although the trace is defined using Plotly's
        choropleth features, we are simply defining our base map.

        The opacity of the map background color should be 0.2.

        Args:
            fig: The figure to add the choropleth trace to
            montreal_data: The data used for the trace
            locations: The locations (neighborhoods) to show on the trace
            z_vals: The table to use for the choropleth's z values
            colorscale: The table to use for the choropleth's color scale
        Returns:
            fig: The updated figure with the choropleth trace

    '''
    fig.add_trace(go.Choroplethmapbox(
        geojson=montreal_data,
        locations=locations,
        z=z_vals,
        featureidkey='properties.NOM',
        colorscale=colorscale,
        showscale=False,
        marker_opacity=0.2,
        marker_line_width=1,
        marker_line_color='#000000',
        hovertemplate=hover.map_base_hover_template(),
    ))
    return fig


def add_scatter_traces(fig, street_df):
    '''
        Adds the scatter trace, representing Montreal's pedestrian paths.

        The marker size should be 20.

        Args:
            fig: The figure to add the scatter trace to
            street_df: The dataframe containing the information on the
                pedestrian paths to display
        Returns:
            The figure now containing the scatter trace

    '''
    colors = px.colors.qualitative.Plotly
    groups = street_df.groupby('properties.TYPE_SITE_INTERVENTION', sort=False)

    for (site_type, subset), color in zip(groups, colors):
        fig.add_trace(go.Scattermapbox(
            lat=subset['properties.LATITUDE'],
            lon=subset['properties.LONGITUDE'],
            mode='markers',
            marker=dict(size=20, color=color),
            name=site_type,
            customdata=subset[['properties.NOM_PROJET',
                               'properties.MODE_IMPLANTATION',
                               'properties.OBJECTIF_THEMATIQUE']].values,
            hovertemplate=hover.map_marker_hover_template(site_type),
        ))
    return fig
