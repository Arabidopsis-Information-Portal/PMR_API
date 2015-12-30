# file: main.py

# optional: import python libraries such as 'import json'
import requests

PMR_BASE_URL = 'http://pmr-webapi.gdcb.iastate.edu/pmrWebApi/api/v1'
PMR_SERVICE = '/boxplot'
PMR_QUERY = '/species=Arabidopsis_thaliana&expId=106&omicsType=valMetabolomics&pId=84&mId=4349&dataVersion=1.0&minLod=true&legendColor=sampleName/'
PMR_FULL_URL = 'http://pmr-webapi.gdcb.iastate.edu/pmrWebApi/api/v1/boxplot/species=Arabidopsis_thaliana&expId=106&omicsType=valMetabolomics&pId=84&mId=4349&dataVersion=1.0&minLod=true&legendColor=sampleName/'

def list(args):
    """
    List metabolite IDs accepted by search().
    """
    print '{"mID":4383}'

def search(args):
    """
    The search(args) function implements the /search endpoint of the web service.
    The args are taken from the URL of an HTTP GET.
    Call the remote service.
    On success, print the JSON payload to STDOUT.
    """
    if args == None:
        # Back door.
        # Just during our development phase, the return is hard-coded.
        # The following value is sample data to draw an actual box plot with plotly.
        print '{"x":{"data":[{"type":"box","inherit":true,"x":["WILD TYPE_E1_IH","WILD TYPE_E1_IH","WILD TYPE_E1_IH","WILD TYPE_E1_IH","WILD TYPE_E1_IH","WILD TYPE_E1_IH"],"y":[0.095,0.008,0.023,0.017,0.043,0.034],"name":"WILD TYPE_E1_IH","marker":{"color":"#DDDE62"}},{"type":"box","inherit":true,"x":["WILD TYPE (E1)-2","WILD TYPE (E1)-2","WILD TYPE (E1)-2","WILD TYPE (E1)-2","WILD TYPE (E1)-2","WILD TYPE (E1)-2"],"y":[0.029,0.065,0.026,0.008,0.017,0.02],"name":"WILD TYPE (E1)-2","marker":{"color":"#706B77"}},{"type":"box","inherit":true,"x":["WILD TYPE (E1)-1","WILD TYPE (E1)-1","WILD TYPE (E1)-1","WILD TYPE (E1)-1","WILD TYPE (E1)-1","WILD TYPE (E1)-1"],"y":[0.034,0.02,0.011,0.021,0.017,0.036],"name":"WILD TYPE (E1)-1","marker":{"color":"#81C1D2"}},{"type":"box","inherit":true,"x":["AT5G66550","AT5G66550","AT5G66550","AT5G66550","AT5G66550","AT5G66550"],"y":[0.017,0.009,0.009,0.015,0.024,0.061],"name":"AT5G66550","marker":{"color":"#EFE9DF"}},{"type":"box","inherit":true,"x":["AT5G51420","AT5G51420","AT5G51420","AT5G51420","AT5G51420","AT5G51420"],"y":[0.037,0.021,0.012,0.029,0.03,0.034],"name":"AT5G51420","marker":{"color":"#6B492E"}},{"type":"box","inherit":true,"x":["AT5G45300","AT5G45300","AT5G45300","AT5G45300","AT5G45300","AT5G45300"],"y":[0.035,0.009,0.03,0.022,0.029,0.034],"name":"AT5G45300","marker":{"color":"#7D956B"}},{"type":"box","inherit":true,"x":["AT5G43380","AT5G43380","AT5G43380","AT5G43380","AT5G43380","AT5G43380"],"y":[0.024,0.008,0.125,0.012,0.015,0.033],"name":"AT5G43380","marker":{"color":"#E1862D"}},{"type":"box","inherit":true,"x":["AT5G40010","AT5G40010","AT5G40010","AT5G40010","AT5G40010","AT5G40010"],"y":[0.038,0.009,0.012,0.023,0.027,0.117],"name":"AT5G40010","marker":{"color":"#6A793C"}},{"type":"box","inherit":true,"x":["AT5G37830","AT5G37830","AT5G37830","AT5G37830","AT5G37830","AT5G37830"],"y":[0.019,0.024,0.026,0.028,0.028,0.031],"name":"AT5G37830","marker":{"color":"#61B3EC"}},{"type":"box","inherit":true,"x":["AT5G16370","AT5G16370","AT5G16370","AT5G16370","AT5G16370","AT5G16370"],"y":[0.027,0.009,0.016,0.022,0.017,0.034],"name":"AT5G16370","marker":{"color":"#497456"}},{"type":"box","inherit":true,"x":["AT5G15530","AT5G15530","AT5G15530","AT5G15530","AT5G15530","AT5G15530"],"y":[0.041,0.024,0.025,0.013,0.029,0.029],"name":"AT5G15530","marker":{"color":"#A3707C"}},{"type":"box","inherit":true,"x":["AT5G13930","AT5G13930","AT5G13930","AT5G13930","AT5G13930","AT5G13930"],"y":[0.035,0.019,0.011,0.025,0.003,0.035],"name":"AT5G13930","marker":{"color":"#64C6A6"}},{"type":"box","inherit":true,"x":["AT4G39520","AT4G39520","AT4G39520","AT4G39520","AT4G39520","AT4G39520"],"y":[0.028,0.034,0.023,0.023,0.018,0.033],"name":"AT4G39520","marker":{"color":"#7C8118"}},{"type":"box","inherit":true,"x":["AT4G14930","AT4G14930","AT4G14930","AT4G14930","AT4G14930","AT4G14930"],"y":[0.038,0.009,0.023,0.022,0.025,0.036],"name":"AT4G14930","marker":{"color":"#8A617C"}},{"type":"box","inherit":true,"x":["AT3G56130","AT3G56130","AT3G56130","AT3G56130","AT3G56130","AT3G56130"],"y":[0.031,0.016,0.057,0.026,0.018,0.072],"name":"AT3G56130","marker":{"color":"#287570"}},{"type":"box","inherit":true,"x":["AT3G49310","AT3G49310","AT3G49310","AT3G49310","AT3G49310","AT3G49310"],"y":[0.026,0.014,0.02,0.02,0.02,0.033],"name":"AT3G49310","marker":{"color":"#372B20"}},{"type":"box","inherit":true,"x":["AT3G16950","AT3G16950","AT3G16950","AT3G16950","AT3G16950","AT3G16950"],"y":[0.009,0.012,0.023,0.028,0.036,0.019],"name":"AT3G16950","marker":{"color":"#5B7E06"}},{"type":"box","inherit":true,"x":["AT2G46180","AT2G46180","AT2G46180","AT2G46180","AT2G46180","AT2G46180"],"y":[0.03,0.021,0.017,0.023,0.021,0.03],"name":"AT2G46180","marker":{"color":"#B7D6DD"}},{"type":"box","inherit":true,"x":["AT2G27490","AT2G27490","AT2G27490","AT2G27490","AT2G27490","AT2G27490"],"y":[0.028,0.012,0.022,0.033,0.027,0.03],"name":"AT2G27490","marker":{"color":"#034850"}},{"type":"box","inherit":true,"x":["AT2G17650","AT2G17650","AT2G17650","AT2G17650","AT2G17650","AT2G17650"],"y":[0.021,0.024,0.033,0.019,0.008,0.028],"name":"AT2G17650","marker":{"color":"#9DB235"}},{"type":"box","inherit":true,"x":["AT2G01170","AT2G01170","AT2G01170","AT2G01170","AT2G01170","AT2G01170"],"y":[0.029,0.009,0.013,0.013,0.021,0.039],"name":"AT2G01170","marker":{"color":"#644C53"}},{"type":"box","inherit":true,"x":["AT1G60230","AT1G60230","AT1G60230","AT1G60230","AT1G60230","AT1G60230"],"y":[0.016,0.017,0.025,0.041,0.038,0.031],"name":"AT1G60230","marker":{"color":"#8B4639"}},{"type":"box","inherit":true,"x":["AT1G52670_1H","AT1G52670_1H","AT1G52670_1H","AT1G52670_1H","AT1G52670_1H","AT1G52670_1H"],"y":[0.024,0.002,0.021,0.044,0.027,0.02],"name":"AT1G52670_1H","marker":{"color":"#703323"}},{"type":"box","inherit":true,"x":["AT1G52670","AT1G52670","AT1G52670","AT1G52670","AT1G52670","AT1G52670"],"y":[0.034,0.034,0.019,0.021,0.023,0.028],"name":"AT1G52670","marker":{"color":"#4D7C97"}},{"type":"box","inherit":true,"x":["AT1G22430","AT1G22430","AT1G22430","AT1G22430","AT1G22430","AT1G22430"],"y":[0.034,0.015,0.012,0.015,0.035,0.036],"name":"AT1G22430","marker":{"color":"#85C685"}},{"type":"box","inherit":true,"x":["AT1G10670","AT1G10670","AT1G10670","AT1G10670","AT1G10670","AT1G10670"],"y":[0.036,0.018,0.022,0.025,0.013,0.026],"name":"AT1G10670","marker":{"color":"#F88665"}}],"layout":{"xaxis":{"zeroline":true,"showline":false,"autorange":true,"showticklabels":false,"showgrid":false,"title":"Sample","titlefont":{"family":"Courier New, monospace","size":14},"showticklabels.1":"false","exponentformat":"e","showexponent":"All","tickangle":20,"autotick":true,"ticks":"outside","tick0":0,"dtick":0.25,"ticklen":1,"tickwidth":4,"tickcolor":"#000","autorange.1":"reversed"},"yaxis":{"title":"Abundance"},"margin":{"b":100,"l":50,"t":120,"r":50,"pad":4},"legend":{"traceorder":"normal"},"boxmode":"overlay","title":"<a href=\'http://www.metnetdb.org/PMR/metabolites/?id=4383\'>Metabolite: icosanoic acid</a><br>Platform: Fatty Acids [Nikolau lab]","hovermode":"closest"},"url":{},"width":{},"height":{},"layout.1":{"xaxis":{"zeroline":true,"showline":false,"autorange":true,"showticklabels":false,"showgrid":false,"title":"Sample","titlefont":{"family":"Courier New, monospace","size":14},"showticklabels.1":"false","exponentformat":"e","showexponent":"All","tickangle":20,"autotick":true,"ticks":"outside","tick0":0,"dtick":0.25,"ticklen":1,"tickwidth":4,"tickcolor":"#000","autorange.1":"reversed"},"yaxis":{"title":"Abundance"},"margin":{"l":50,"r":50,"b":100,"t":120,"pad":4},"legend":{"traceorder":"normal"},"boxmode":"overlay","title":"<a href=\'http://www.metnetdb.org/PMR/metabolites/?id=4383\'>Metabolite: icosanoic acid</a><br>Platform: Fatty Acids [Nikolau lab]","hovermode":"closest"},"filename":"<a href=\'http://www.metnetdb.org/PMR/metabolites/?id=4383\'>Metabolite: icosanoic acid</a><br>Platform: Fatty Acids [Nikolau lab]"},"evals":[]}'
        print "---"
        return

    # Parse the parameter args.
    # Expect type dictionary.
    # Expect the dictionary defines mID etc.
    # metaboliteID = args['mID']

    # If the remote service indicates success (200) then pass along the payload.
    # Assume the payload is a JSON object.
    remoteURL = PMR_BASE_URL + PMR_SERVICE + PMR_QUERY
    # For debug, uncomment...
    #print remoteURL
    #print '---'
    response = requests.get(remoteURL, verify=False)
    if response.status_code==200:
        # Do not output JSON. Let Adama environment format this.
        #print response.json()
        #print '---'
        print response.text
        print '---'

# For interactive test, uncomment this call.
search('4383')
list('metabolite')
