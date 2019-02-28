from bokeh.embed import components
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.sampledata.sea_surface_temperature import sea_surface_temperature
from django.shortcuts import render

# Create your views here.
def generate_plot(request):

    df = sea_surface_temperature.copy()
    source = ColumnDataSource(data=df)

    plot = figure(x_axis_type='datetime', y_range=(0, 25), y_axis_label='Temperature (Celsius)',
                  title="Sea Surface Temperature")
    plot.line('time', 'temperature', source=source)

    script, div = components(plot, CDN)

    return render(request, "sea_temperature.html", {"script_data": script, "div_data": div})