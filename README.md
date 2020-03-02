# Python/Flask tutorial sample for Visual Studio Code

* This sample contains the completed program from the tutorial, make sure to visit the link: [Using Flask in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-flask). Intermediate steps are not included.
* This application is ready to be Dockerized and run in a container. For steps, see [Python in containers](https://code.visualstudio.com/docs/containers/quickstart-python).

To run the sample:

1. In VS Code Terminal, run `python -m venv env` to create a virtual environment as described in the tutorial.
2. Press Ctrl + Shift + P and run command `Python: Select Interpreter`.
3. Activate the virtual environment by running `source env/bin/activate` (Linux/MacOS) or `env/scripts/activate` (Windows).
4. In terminal, run `pip install django`.
5. From Run and Debug section, select `Python: Flask` task and hit F5.

## Contributing

Contributions to the sample are welcome. When submitting changes, also consider submitting matching changes to the tutorial, the source file for which is [tutorial-flask.md](https://github.com/Microsoft/vscode-docs/blob/master/docs/python/tutorial-flask.md).

Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot automatically determines whether you need to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

## Additional details

* This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
* For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
* Contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
