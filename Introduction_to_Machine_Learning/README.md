# Introduction to Machine Learning

**Instructor and author.** Diaeddin Rimawi (<dmrimawi@gmail.com>)  
**Prerequisites.** Basic familiarity with Python is helpful. No previous knowledge of Machine Learning, Data Science, statistics, or probability is assumed.

## Overview

How can a computer learn to make a useful prediction from previous examples? We will begin with familiar problems, such as estimating delivery times, and gradually discover how data can help us describe situations, identify patterns, and build predictive models.

The course follows an **example-driven, progressive approach**. We will first understand the problem and its data, then use small Python examples to investigate possible solutions. As the course progresses, we will study how different learning methods work, what they can and cannot tell us, and how to evaluate their results. **Understanding and interpreting results is as important as writing code.**

Lecture materials are provided primarily as interactive **Jupyter notebooks**. Each notebook combines explanations, runnable Python code, visualizations, questions, and short experiments. You can read the explanations without executing code, but running and changing examples is strongly encouraged.

### Intended learning outcomes

By the end of the course, students should be able to:

- Describe the relationship between Data Science, Artificial Intelligence, Machine Learning, and Deep Learning.
- Understand and explore datasets, use basic statistics and visualizations, and recognize data-quality concerns.
- Prepare data and choose useful features for Machine Learning tasks.
- Distinguish regression, classification, clustering, anomaly detection, semi-supervised learning, active learning, and reinforcement learning.
- Train and evaluate introductory Machine Learning models and discuss the reliability of their predictions.
- Explain how simple artificial neural networks learn and train a neural network using Python tools.
- Choose a suitable learning approach for a practical question and clearly communicate its limitations.

## Course topics

| Part | Topic | Hours |
|---|---|---:|
| 1 | Data Science Foundations | 12 |
| 2 | Data Preprocessing and Proximity Measures | 8 |
| 3 | Supervised Learning: Regression and Classification | 16 |
| 4 | Unsupervised Learning: Clustering and Anomaly Detection | 6 |
| 5 | Semi-Supervised and Active Learning | 2 |
| 6 | Reinforcement Learning using Q-Tables | 4 |
| 7 | Artificial Neural Networks and Deep Learning Overview | 12 |
| | **Total** | **60** |

## Table of contents and lecture schedule

Course materials will be added to the corresponding week folder as lectures become available. Only published materials are linked below.

| Week | Dates | First lecture | Second lecture |
|---|---|---|---|
| **[W1](./W1/)** | 17 & 20 Oct 2026 | **[L01 — From Data to Knowledge: Introduction to Data Science and ML](./W1/L01_From_Data_to_Knowledge.ipynb)** | **[L02 — Understanding Data: Types, Features, and NumPy Essentials](./W1/L02_Understanding_Data_and_NumPy.ipynb)** |
| **[W2](./W2/)** | 24 & 27 Oct 2026 | **[L03 — Exploring and Manipulating Data with Pandas](./W2/L03_Exploring_and_Manipulating_Data_with_Pandas.ipynb)** | **[L04 — Visualizing Data and Discovering Patterns](./W2/L04_Visualizing_Data_and_Discovering_Patterns.ipynb)** |
| W3 | 31 Oct & 3 Nov 2026 | L05 — Descriptive Statistics for Data Science | L06 — Probability, Distributions, and Sampling |
| W4 | 7 & 10 Nov 2026 | L07 — Data Quality: Cleaning and Understanding Imperfect Data | L08 — Feature Engineering: Transforming Data for Learning |
| W5 | 14 & 17 Nov 2026 | L09 — Measuring Similarity: Distances and Proximity Measures | L10 — Feature Selection, PCA, and Reliable Preprocessing Pipelines |
| W6 | 21 & 24 Nov 2026 | L11 — Linear Regression: Predicting Continuous Values | L12 — Understanding Regression Errors and Model Complexity |
| W7 | 28 Nov & 1 Dec 2026 | L13 — Logistic Regression: Learning to Classify | L14 — Understanding and Evaluating Classification Models |
| W8 | 5 & 8 Dec 2026 | L15 — K-Nearest Neighbors: Classification Through Similarity | L16 — Decision Trees: Learning from Rules and Information |
| W9 | 12 & 15 Dec 2026 | L17 — Random Forests: Learning from Multiple Models | L18 — Support Vector Machines and Comparing Classifiers |
| W10 | 19 & 22 Dec 2026 | L19 — K-Means Clustering: Discovering Hidden Groups | L20 — Evaluating Clusters and Exploring DBSCAN |
| W11 | 26 & 29 Dec 2026 | L21 — Isolation Forest: Discovering Anomalies in Data | L22 — Learning with Limited Labels: Semi-Supervised and Active Learning |
| W12 | 2 & 5 Jan 2027 | L23 — Reinforcement Learning: Learning Through Rewards | L24 — Q-Learning: Building Intelligent Agents with Q-Tables |
| W13 | 9 & 12 Jan 2027 | L25 — The Perceptron: Understanding the First Artificial Neuron | L26 — Learning from Errors: Loss Functions, Delta Rule, and Gradient Descent |
| W14 | 16 & 19 Jan 2027 | L27 — Multilayer Perceptrons: Building Neural Networks | L28 — Backpropagation: How Neural Networks Actually Learn |
| W15 | 23 & 26 Jan 2027 | L29 — Training Neural Networks with Keras and Modern Optimizers | L30 — Designing Effective Neural Networks: From MLPs to Deep Learning |


## Getting started: Python and Jupyter

The lectures run as Jupyter notebooks (`.ipynb` files). Jupyter lets you read the notes, execute one Python cell at a time, and experiment with values while keeping explanations and code in the same document.

### 1. Install Python and get the course files

Install a recent version of **Python 3** (Python 3.11 or newer is recommended) from [python.org](https://www.python.org/downloads/). On Windows, ensure Python is accessible from the terminal (for example, by using the Python launcher `py`).

Clone the repository with Git, or download it as a ZIP from GitHub and extract it:

```bash
git clone https://github.com/dmrimawi/courses-library.git
cd courses-library/Introduction_to_Machine_Learning
```

If you downloaded a ZIP, open a terminal in the extracted `Introduction_to_Machine_Learning` folder instead. All remaining commands should be run from **this course folder**.

### 2. Create a virtual environment named `venv`

A *virtual environment* keeps the packages used for this course separate from other Python projects.

**Windows (PowerShell or Command Prompt):**

```powershell
py -m venv venv
```

**macOS or Linux:**

```bash
python3 -m venv venv
```

The new `venv/` folder is local to your machine and should not be committed to Git.

### 3. Activate the virtual environment

Use the command for your terminal:

**Windows — PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows — Command Prompt:**

```bat
venv\Scripts\activate.bat
```

**macOS or Linux:**

```bash
source venv/bin/activate
```

Your terminal will normally display `(venv)` at the beginning of the prompt. On Windows, if PowerShell blocks script activation, use Command Prompt instead.

### 4. Install Jupyter and the Python libraries

While `venv` is active, run:

```bash
python -m pip install --upgrade pip
python -m pip install jupyterlab notebook ipykernel numpy pandas matplotlib scikit-learn
```

- **JupyterLab** and **Jupyter Notebook** let you open and run `.ipynb` lecture files. Either interface works.
- **ipykernel** lets Jupyter execute notebook code using Python.
- **NumPy**, **pandas**, **Matplotlib**, and **scikit-learn** support the demonstrations in L01 and later lectures. Their roles are introduced gradually in class.

No external datasets, accounts, or API keys are required for L01.

### 5. Open and run Lecture 01

From the course folder, with `venv` still active, start **one** of the following:

**Option A — JupyterLab:**

```bash
jupyter lab
```

**Option B — Classic Jupyter Notebook interface:**

```bash
jupyter notebook
```

Jupyter will open in your browser (or print a local URL that you can open). Navigate to the `W1` folder and select `L01_From_Data_to_Knowledge.ipynb`.

Use the **Python 3** kernel from your environment. Run cells in order using **Shift + Enter**, or use **Run All** to execute the whole notebook. Read the Markdown explanations and examine each output before moving on.

**If an import fails:** Check that `venv` is active, that the installation command in Step 4 finished successfully, and that the notebook is using the same environment. You can verify the active Python by running `python -m pip --version` in your terminal.

### 6. Finish your session

Stop the Jupyter server in the terminal with **Ctrl + C**. To leave the environment, run:

```bash
deactivate
```

Next time, enter the course folder, activate the same `venv`, and launch Jupyter again. You do not need to reinstall everything for every lecture.

## Weekly learning and assignments

Each week consists of two two-hour lectures (Saturday and Tuesday). Short interactive questions and experiments are included in the notebooks. **One short assignment is assigned after Tuesday's lecture each week**, connecting the two lectures and introducing a small challenge related to the following week.


## Notes and acknowledgments

- These materials are provided for learning and free reuse under the repository's [license](../LICENSE.md). Corrections and improvements are welcome through issues and pull requests.
- I would like to thank Prof. Antonio Liotta (Free University of Bozen-Bolzano) for generously sharing his teaching materials, which have served as a source of inspiration for this course.
