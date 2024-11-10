const tools = [
	{
		name: "autoflake",
		description:
			"Automatically removes unused imports and variables from Python code to ensure cleaner and more efficient scripts.",
		tags: ["code quality"],
		link: "/docs/tools/autoflake",
		image: "/img/icons/autoflake.webp",
	},
	{
		name: "autopep8",
		description:
			"Formats Python code automatically to adhere to PEP 8 standards, improving readability and consistency.",
		tags: ["code quality"],
		link: "./autopep8",
		image: "/img/icon/autopep8.svg",
	},
	{
		name: "docusaurus",
		description:
			"A powerful and customizable static site generator for building documentation websites efficiently.",
		tags: ["docs"],
		link: "./docusaurus",
		image: "/img/icon/docusaurus.svg",
	},
	{
		name: "fastapi",
		description:
			"A modern, high-performance web framework for building APIs with Python, based on standard Python type hints.",
		tags: ["framework"],
		link: "./fastapi",
		image: "/img/icon/fastapi.svg",
	},
	{
		name: "fontawesome",
		description:
			"A widely-used toolkit for adding scalable vector icons and social logos to web projects.",
		tags: ["icons"],
		link: "./fontawesome",
		image: "/img/icon/fontawesome.svg",
	},
	{
		name: "framer-motion",
		description:
			"A popular React library for creating advanced animations and transitions with ease.",
		tags: ["animations"],
		link: "./framer-motion",
		image: "/img/icon/framer-motion.svg",
	},
	{
		name: "hypothesis",
		description:
			"Implements property-based testing in Python, helping discover edge cases by generating test cases dynamically.",
		tags: ["testing"],
		link: "./hypothesis",
		image: "/img/icon/hypothesis.svg",
	},
	{
		name: "ipykernel",
		description:
			"Provides the IPython kernel for Jupyter, facilitating code execution and interaction within notebooks.",
		tags: ["notebooks"],
		link: "./ipykernel",
		image: "/img/icon/ipykernel.svg",
	},
	{
		name: "ipywidgets",
		description:
			"Enables interactive widgets in Jupyter Notebooks for dynamic user input and data visualization.",
		tags: ["UI"],
		link: "./ipywidgets",
		image: "/img/icon/ipywidgets.svg",
	},
	{
		name: "isort",
		description:
			"Automates the sorting of imports alphabetically and organizes them into logical sections for better code structure.",
		tags: ["code quality"],
		link: "./isort",
		image: "/img/icon/isort.svg",
	},
	{
		name: "jupyter-contrib-nbextensions",
		description:
			"Offers an array of extensions to enhance Jupyter Notebook functionality and customization.",
		tags: ["notebooks"],
		link: "./jupyter-contrib-nbextensions",
		image: "/img/icon/jupyter-contrib-nbextensions.svg",
	},
	{
		name: "jupyter-nbextensions-configurator",
		description:
			"Allows easy configuration and management of nbextensions within Jupyter Notebook.",
		tags: ["notebooks"],
		link: "./jupyter-nbextensions-configurator",
		image: "/img/icon/jupyter-nbextensions-configurator.svg",
	},
	{
		name: "jupyterlab",
		description:
			"An advanced user interface for Jupyter, providing a flexible, modern environment for interactive computing.",
		tags: ["notebooks"],
		link: "./jupyterlab",
		image: "/img/icon/jupyterlab.svg",
	},
	{
		name: "jupyterlab-git",
		description:
			"Brings Git integration into JupyterLab, enabling version control directly within the interface.",
		tags: ["version control"],
		link: "./jupyterlab-git",
		image: "/img/icon/jupyterlab-git.svg",
	},
	{
		name: "jupyterlab-github",
		description:
			"Facilitates seamless integration between JupyterLab and GitHub, enabling collaborative development.",
		tags: ["version control"],
		link: "./jupyterlab-github",
		image: "/img/icon/jupyterlab-github.svg",
	},
	{
		name: "loguru",
		description:
			"A feature-rich logging library for Python, designed to be simple yet powerful, improving the development experience.",
		tags: ["logging"],
		link: "./loguru",
		image: "/img/icon/loguru.svg",
	},
	{
		name: "lucide-react",
		description:
			"An open-source icon library that delivers consistent and elegant icons for React projects.",
		tags: ["icons"],
		link: "./lucide-react",
		image: "/img/icon/lucide-react.svg",
	},
	{
		name: "matplotlib",
		description:
			"A foundational Python library for creating static, animated, and interactive 2D plots.",
		tags: ["data visualization"],
		link: "./matplotlib",
		image: "/img/icon/matplotlib.svg",
	},
	{
		name: "mypy",
		description:
			"Enables optional static typing for Python code, enhancing type safety and reducing potential runtime errors.",
		tags: ["code analysis"],
		link: "./mypy",
		image: "/img/icon/mypy.svg",
	},
	{
		name: "nbconvert",
		description:
			"Converts Jupyter Notebooks to various formats such as HTML, PDF, and Markdown for versatile sharing.",
		tags: ["notebooks"],
		link: "./nbconvert",
		image: "/img/icon/nbconvert.svg",
	},
	{
		name: "nbdime",
		description:
			"Specialized tools for diffing and merging Jupyter notebooks, maintaining notebook integrity.",
		tags: ["version control"],
		link: "./nbdime",
		image: "/img/icon/nbdime.svg",
	},
	{
		name: "nest-asyncio",
		description:
			"Allows nesting of asyncio event loops in Python, facilitating complex asynchronous use cases.",
		tags: ["asyncio"],
		link: "./nest-asyncio",
		image: "/img/icon/nest-asyncio.svg",
	},
	{
		name: "pandas",
		description:
			"A robust data analysis library providing flexible data structures like DataFrames for efficient data manipulation.",
		tags: ["data analysis"],
		link: "./pandas",
		image: "/img/icon/pandas.svg",
	},
	{
		name: "plotly",
		description:
			"Creates interactive, publication-quality graphs and charts with ease, supporting multiple chart types and customizations.",
		tags: ["data visualization"],
		link: "./plotly",
		image: "/img/icon/plotly.svg",
	},
	{
		name: "plotly dash",
		description:
			"A Python framework for building analytical web applications and dashboards with Plotly for visualization.",
		tags: ["dashboarding"],
		link: "./plotly-dash",
		image: "/img/icon/plotly-dash.svg",
	},
	{
		name: "poetry",
		description:
			"Simplifies Python dependency management and project packaging for streamlined development workflows.",
		tags: ["dependency management"],
		link: "./poetry",
		image: "/img/icon/poetry.svg",
	},
	{
		name: "pydantic",
		description:
			"Leverages Python type annotations for powerful data validation and parsing.",
		tags: ["data validation"],
		link: "./pydantic",
		image: "/img/icon/pydantic.svg",
	},
	{
		name: "pydantic-settings",
		description:
			"An extension of Pydantic for managing application configuration through type-safe settings.",
		tags: ["configuration"],
		link: "./pydantic-settings",
		image: "/img/icon/pydantic-settings.svg",
	},
	{
		name: "pylint",
		description:
			"A comprehensive static code analysis tool for detecting programming errors and enforcing coding standards.",
		tags: ["code analysis"],
		link: "./pylint",
		image: "/img/icon/pylint.svg",
	},
	{
		name: "pytest",
		description:
			"A feature-rich testing framework for writing and running unit tests in Python.",
		tags: ["testing"],
		link: "./pytest",
		image: "/img/icon/pytest.svg",
	},
	{
		name: "pytest-benchmark",
		description:
			"Measures the performance of code during testing, allowing developers to monitor speed and optimize as needed.",
		tags: ["performance"],
		link: "./pytest-benchmark",
		image: "/img/icon/pytest-benchmark.svg",
	},
	{
		name: "pytest-cov",
		description:
			"Integrates code coverage analysis into pytest runs, providing insight into which parts of the code are tested.",
		tags: ["testing"],
		link: "./pytest-cov",
		image: "/img/icon/pytest-cov.svg",
	},
	{
		name: "pytest-emoji",
		description:
			"A fun pytest plugin that adds emojis to test outputs for better readability and a touch of personality.",
		tags: ["UI"],
		link: "./pytest-emoji",
		image: "/img/icon/pytest-emoji.svg",
	},
	{
		name: "pytest-html",
		description:
			"Generates comprehensive HTML reports for pytest results, making it easier to share and review test summaries.",
		tags: ["reporting"],
		link: "./pytest-html",
		image: "/img/icon/pytest-html.svg",
	},
	{
		name: "pytest-icdiff",
		description:
			"Displays side-by-side diffs when pytest tests fail, enhancing the visibility of differences.",
		tags: ["testing"],
		link: "./pytest-icdiff",
		image: "/img/icon/pytest-icdiff.svg",
	},
	{
		name: "pytest-instafail",
		description:
			"Instantly shows failures during pytest runs, providing immediate feedback for faster debugging.",
		tags: ["testing"],
		link: "./pytest-instafail",
		image: "/img/icon/pytest-instafail.svg",
	},
	{
		name: "pytest-mock",
		description:
			"Simplifies the use of mock objects in pytest, facilitating unit testing with controlled test environments.",
		tags: ["testing"],
		link: "./pytest-mock",
		image: "/img/icon/pytest-mock.svg",
	},
	{
		name: "pytest-sugar",
		description:
			"Enhances the UI of pytest, offering a more intuitive and visually appealing test output.",
		tags: ["UI"],
		link: "./pytest-sugar",
		image: "/img/icon/pytest-sugar.svg",
	},
	{
		name: "pytest-timeout",
		description:
			"Aborts tests that exceed a specified runtime, helping to identify and stop hanging tests.",
		tags: ["performance"],
		link: "./pytest-timeout",
		image: "/img/icon/pytest-timeout.svg",
	},
	{
		name: "pytest-xdist",
		description:
			"Distributes test execution across multiple CPUs, speeding up testing for larger projects.",
		tags: ["performance"],
		link: "./pytest-xdist",
		image: "/img/icon/pytest-xdist.svg",
	},
	{
		name: "python-dotenv",
		description:
			"Loads environment variables from .env files, making environment management simpler and more secure.",
		tags: ["configuration"],
		link: "./python-dotenv",
		image: "/img/icon/python-dotenv.svg",
	},
	{
		name: "react-icons",
		description:
			"Provides easy integration of popular icon packs into React applications for richer UI elements.",
		tags: ["icons"],
		link: "./react-icons",
		image: "/img/icon/react-icons.svg",
	},
	{
		name: "rich",
		description:
			"A Python library that brings beautiful and customizable terminal formatting with features like progress bars and tables.",
		tags: ["UI"],
		link: "./rich",
		image: "/img/icon/rich.svg",
	},
	{
		name: "ruff",
		description:
			"A super-fast Python linter written in Rust, designed to catch common code issues efficiently.",
		tags: ["performance"],
		link: "./ruff",
		image: "/img/icon/ruff.svg",
	},
	{
		name: "scss",
		description:
			"A powerful CSS preprocessor that enhances CSS with variables, nesting, and more advanced features.",
		tags: ["styling"],
		link: "./scss",
		image: "/img/icon/scss.svg",
	},
	{
		name: "seaborn",
		description:
			"A data visualization library built on top of Matplotlib, offering high-level interfaces for drawing informative statistical graphics.",
		tags: ["data visualization"],
		link: "./seaborn",
		image: "/img/icon/seaborn.svg",
	},
	{
		name: "shadcn-ui",
		description:
			"Offers unstyled, highly customizable React components for building accessible and flexible user interfaces.",
		tags: ["UI"],
		link: "./shadcn-ui",
		image: "/img/icon/shadcn-ui.svg",
	},
	{
		name: "tailwindcss",
		description:
			"A utility-first CSS framework that empowers developers to design responsive UIs rapidly.",
		tags: ["styling"],
		link: "./tailwindcss",
		image: "/img/icon/tailwindcss.svg",
	},
	{
		name: "typer",
		description:
			"A Python library for building user-friendly and intuitive command-line interfaces (CLIs) with minimal code.",
		tags: ["CLI"],
		link: "./typer",
		image: "/img/icon/typer.svg",
	},
	{
		name: "yapf",
		description:
			"A Python code formatter developed by Google that reformats code to the best practices outlined in PEP 8.",
		tags: ["code quality"],
		link: "./yapf",
		image: "/img/icon/yapf.svg",
	},
	{
		name: "pyenv",
		description:
			"A simple Python version management tool that allows you to easily switch between multiple versions of Python.",
		tags: ["version management"],
		link: "./pyenv",
		image: "/img/icon/pyenv.svg",
	},
];

export default tools;