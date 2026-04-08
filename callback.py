'''
    This file contains the functions to call when
    a click is detected on the map, depending on the context
'''
import dash_html_components as html


def no_clicks(style):
    '''
        Deals with the case where the map was not clicked

        Args:
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    style['visibility'] = 'hidden'
    return None, None, None, style


def map_base_clicked(title, mode, theme, style):
    '''
        Deals with the case where the map base is
        clicked (but not a marker)

        Args:
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    return title, mode, theme, style


def map_marker_clicked(figure, curve, point, title, mode, theme, style): # noqa : E501 pylint: disable=unused-argument too-many-arguments line-too-long
    '''
        Deals with the case where a marker is clicked

        Args:
            figure: The current figure
            curve: The index of the curve containing the clicked marker
            point: The index of the clicked marker
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    trace = figure['data'][curve]
    color = trace['marker']['color']
    name, implantation, themes = trace['customdata'][point]

    new_title = html.Span(name, style={'color': color})
    new_mode = implantation

    if isinstance(themes, str) and themes.strip():
        items = [line for line in themes.splitlines() if line.strip()]
        new_theme = [html.Div('Thématique :'),
                     html.Ul([html.Li(line) for line in items])]
    else:
        new_theme = None

    new_style = {**style, 'visibility': 'visible'}
    return new_title, new_mode, new_theme, new_style
