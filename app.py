from flask import Flask, render_template, request, redirect
import logic.login as iniciate
import logic.listServers as listServers
import logic.listImages as listImages
import logic.listFlavors as listFlavors
import logic.listNetwork as listNetwork
import logic.createServer as createServer
import logic.listFloating as listFloating


app = Flask(__name__)
token = iniciate.logged('workshop2022@utb.edu.co','ILOVECLOUD2022')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/logging",methods=['POST'])
def logging():
    email = request.form['email']
    password = request.form['password']
    iniciar = iniciate.logged(email,password)
    if(iniciar):
        return redirect('/home')
    else:
        return redirect('/login')

@app.route('/home')
def home():
    servers = listServers.getServers(token)
    return render_template('home.html',value=servers)

@app.route('/create')
def create():
    images = listImages.getImages(token)
    flavors = listFlavors.getFlavors(token)
    networks = listNetwork.getNetworks(token)
    return render_template('createInstance.html',value=[images,flavors,networks])

@app.route('/creating',methods=['POST'])
def creating():
    images = request.form['images']
    flavors = request.form['flavors']
    networks = request.form['network']
    name = request.form['name']
    images = images.split()
    flavors = flavors.split()
    networks = networks.split()
    imagesData = listImages.getImages(token)
    flavorsData = listFlavors.getFlavors(token)
    networksData = listNetwork.getNetworks(token)
    imageId = listImages.findVersion(images[0],images[1],imagesData)
    flavorsId = listImages.findId(flavors[0],flavorsData)
    networksId = listImages.findId(networks[0],networksData)
    createServer.createServer(token,name,imageId,flavorsId,networksId)
    return redirect('/home')

@app.route('/createFloating')
def createFloating():
    servers = listServers.getServers(token)
    floatingips = listFloating.getFloating(token)
    return render_template('createFloating.html',value=[servers,floatingips])

@app.route('/creatingFloating',methods=['POST'])
def creatingFloating():
    servers = listServers.getServers(token)
    ip = request.form['floating']
    server = request.form['server']
    serverId = listServers.findId(server,servers)
    print(serverId)
    listFloating.assignFloating(token,serverId,ip)
    return redirect('/home')

if __name__ == '__main__':
    app.run(debug=True)