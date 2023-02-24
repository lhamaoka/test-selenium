## How to run on Kubernetes

This example shows you how to deploy Selenium to Kubernetes in a scalable fashion.

### Prerequisites

This example assumes you have a working Kubernetes cluster and a properly configured kubectl client. See the [Getting Started Guides](https://kubernetes.io/docs/getting-started-guides/) for details.

Your cluster must have 4 CPU and 6 GB of RAM to complete the example up to the scaling portion.

### Deploy Selenium Grid Hub:

We will be using Selenium Grid Hub to make our Selenium install scalable via a master/worker model. The Selenium Hub is the master, and the Selenium Nodes are the workers(not to be confused with Kubernetes nodes). We only need one hub, but we're using a replication controller to ensure that the hub is always running:

```console
kubectl create --filename=kubernetes/selenium-hub-deployment.yaml
```

The Selenium Nodes will need to know how to get to the Hub, let's create a service for the nodes to connect to.

```console
kubectl create --filename=kubernetes/selenium-hub-svc.yaml
```

### Verify Selenium Hub Deployment

Let's verify our deployment of Selenium hub by connecting to the web console.

#### Kubernetes Nodes Reachable

If your Kubernetes nodes are reachable from your network, you can verify the hub by hitting it on the nodeport. You can retrieve the nodeport by typing `kubectl describe svc selenium-hub`, however the snippet below automates that by using kubectl's template functionality:

```console
export NODEPORT=`kubectl get svc --selector='app=selenium-hub' --output=template --template="{{ with index .items 0}}{{with index .spec.ports 0 }}{{.nodePort}}{{end}}{{end}}"`
export NODE=`kubectl get nodes --output=template --template="{{with index .items 0 }}{{.metadata.name}}{{end}}"`

curl http://$NODE:$NODEPORT
```

#### Kubernetes Nodes Unreachable

If you cannot reach your Kubernetes nodes from your network, you can proxy via kubectl.

```console
export PODNAME=`kubectl get pods --selector="app=selenium-hub" --output=template --template="{{with index .items 0}}{{.metadata.name}}{{end}}"`
kubectl port-forward $PODNAME 4444:4444
```

In a separate terminal, you can now check the status.

```console
curl http://localhost:4444
```

### Deploy Firefox and Chrome Nodes:

Now that the Hub is up, we can deploy workers.

This will deploy 2 Chrome nodes.

```console
kubectl create --filename=kubernetes/selenium-node-chrome-deployment.yaml
```

And 2 Firefox nodes to match.

```console
kubectl create --filename=kubernetes/selenium-node-firefox-deployment.yaml
```


### Scale your Firefox and Chrome nodes.

If you need more Firefox or Chrome nodes, your hardware is the limit:

```console
kubectl scale deployment selenium-node-firefox --replicas=10
kubectl scale deployment selenium-node-chrome --replicas=10
```

You now have 10 Firefox and 10 Chrome nodes, happy Seleniuming!

### Debugging

Sometimes it is necessary to check on a hung test. Each pod is running VNC. To check on one of the browser nodes via VNC, it's recommended that you proxy, since we don't want to expose a service for every pod, and the containers have a weak VNC password. Replace POD_NAME with the name of the pod you want to connect to.

```console
kubectl port-forward $POD_NAME 5900:5900
```

Then connect to localhost:5900 with your VNC client using the password "secret"

Enjoy your scalable Selenium Grid!

Referance: https://github.com/kubernetes/examples/tree/master/staging/selenium

### Teardown

To remove all created resources, run the following:

```console
kubectl delete deployment selenium-hub
kubectl delete deployment selenium-node-chrome
kubectl delete deployment selenium-node-firefox
kubectl delete svc selenium-hub
```
## How to run on GCP using Kubernetes cluster

### Prerequisites

Need to login to GCP and create a kuberneties cluster. I would prefer atleast 3 nodes with atleast 7GB memory.

### Setup kubernetes

Clone from this repositry. Setup deployment and services
```console
git clone https://gitlab.com/benjose22/pytest_selenium.git
cd ~/pytest_selenium/
kubectl create --filename=kubernetes/selenium-hub-deployment.yaml
kubectl create --filename=kubernetes/selenium-hub-svc.yaml
kubectl create --filename=kubernetes/selenium-node-chrome-deployment.yaml
```

### Setup gcloud firewall
```console
export NODEPORT=`kubectl get svc --selector='app=selenium-hub' --output=template --template="{{ with index .items 0}}{{with index .spec.ports 0 }}{{.nodePort}}{{end}}{{end}}"`
export EXTERNAL_IP=`kubectl get nodes -o jsonpath='{ $.items[0].status.addresses[?(@.type=="ExternalIP")].address }'`
gcloud compute firewall-rules create test-node-port --allow tcp:$NODEPORT
curl http://$EXTERNAL_IP:$NODEPORT
```
### Execute the pytest selenium script
I have scaled up to 5 chrome deployments and executing the container.
```console
kubectl scale deployment selenium-node-chrome --replicas=5

docker build -t pytest-with-src -f pytest.Dockerfile .
docker run --network="host" --rm pytest-with-src --browser "chrome" --executor $EXTERNAL_IP:$NODEPORT
```
### Teardown
Delete the firewall, remove the Docker image and delete all the kubernetes development and services.
```console
gcloud compute firewall-rules delete test-node-port
docker rmi pytest-with-src
kubectl delete deployment selenium-hub
kubectl delete deployment selenium-node-chrome
kubectl delete svc selenium-hub
```
