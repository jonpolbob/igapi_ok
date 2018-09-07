# Lightstreamer - Basic Stock-List Demo - Python Client

This project contains a simple Python script that shows a minimal client-side implementation of the [Lightstreamer Server Text mode Protocol](http://www.lightstreamer.com/docs/client_generic_base/Network%20Protocol%20Tutorial.pdf).

![screenshot](screen_python_large.png)

## Details

The example provides a very simple version of the [Stock-List Demos](https://github.com/Lightstreamer/Lightstreamer-example-Stocklist-client-javascript), where a single subscription to 12 items is submitted.
The updates are then formatted and displayed on the console.
  
The script shows all the basic steps required to establish an interaction to Lightstreamer Server. More specifically, the code comprises these actions: 

* Connection to Lightstreamer server and session creation
* Subscription to items with specified fields
* Notification about real time updates
* Unsubscription from items
* Final disconnection 

It is important to highlight that the example is not meant to be a complete and robust Lightstreamer Client Python library, but it could be used as a starting point to build more complex interactions with the Lightstreamer server to manage all the possible scenarios included in the protocol.

## Install

If you want to install a version of this demo pointing to your local Lightstreamer Server, follow these steps:

* Note that, as prerequisite, the [Lightstreamer - Stock- List Demo - Java Adapter](https://github.com/Lightstreamer/Lightstreamer-example-Stocklist-adapter-java) has to be deployed on your local Lightstreamer Server instance. Please check out that project and follow the installation instructions provided with it.
* Launch Lightstreamer Server.
* Go to [http://python.org/download/](http://python.org/download/) and download the appropriate **Python** (tested since version 2.6.3) for your OS and follow the instructions to install it on your system. Note that the demo currently **can not** be launched from IDLE.

You can now run the Python script simply executing the following commands on different OS:
	
* Windows machines:

```
start python /path/to/example/stock_list_demo.py
```

* Linux machines: 

```
python /path/to/example/stock_list_demo.py
```
or, alternatively, you can make the script executable:

```
chmod +x /path/to/example/stock_list_demo.py
```

and then type:
```
/path/to/example/stock_list_demo.py
```

The example is configured to connect to http://push.lightstreamer.com:80, but you can easily change these settings modifying the following line:

```lightstreamer_client = LSClient("http://push.lightstreamer.com:80", "DEMO")```

to connect to the correct combination of host and port of your Lightstreamer server.

## See Also

* [A Python Client Example for Lightstreamer](http://blog.lightstreamer.com/2015/01/a-python-client-example-for_14.html)

### Lightstreamer Adapters Needed by this Demo Client

<!-- START RELATED_ENTRIES -->
* [Lightstreamer - Stock- List Demo - Java Adapter](https://github.com/Lightstreamer/Lightstreamer-example-Stocklist-adapter-java)

<!-- END RELATED_ENTRIES -->

### Related Projects

* [Lightstreamer - Stock-List Demos - HTML Clients](https://github.com/Lightstreamer/Lightstreamer-example-Stocklist-client-javascript)
* [Lightstreamer - Basic Stock-List Demo - jQuery (jqGrid) Client](https://github.com/Lightstreamer/Lightstreamer-example-StockList-client-jquery)
* [Lightstreamer - Stock-List Demo - Dojo Toolkit Client](https://github.com/Lightstreamer/Lightstreamer-example-StockList-client-dojo)
* [Lightstreamer - Basic Stock-List Demo - Java SE (Swing) Client](https://github.com/Lightstreamer/Lightstreamer-example-StockList-client-java)
* [Lightstreamer - Basic Stock-List Demo - .NET Client](https://github.com/Lightstreamer/Lightstreamer-example-StockList-client-dotnet)
* [Lightstreamer - Stock-List Demos - Flex Clients](https://github.com/Lightstreamer/Lightstreamer-example-StockList-client-flex)

## Lightstreamer Compatibility Notes

* Compatible with Lightstreamer server since version 6.0.
* Ensure that Generic Client API is supported by Lightstreamer Server license configuration.
* For a version of this example compatible with Lightstreamer server version 5.1.2, please refer to [this tag](https://github.com/Lightstreamer/Lightstreamer-example-StockList-client-python/tree/v1.0).
