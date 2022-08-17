# Health Insurance Cross Sell Prediction

This project focus on creating a sorted list of customers likely to purchase another type of insurance based on old customers' information.

<img src=Images/car-insurance.jpg width="450" height="250"/>

<p><strong>Disclaimer</strong>: this project was inspired by the &quot;Health Insurance Cross Sell Prediction&quot; challenge published on <a href="https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction">kaggle</a>. It is a fictitious project. However; the steps followed to solve the business problem are the same applied to real projects.</p>

<h1 dir="auto">Business problem</h1>
<p>This project is to meet an insurance company demand that has provided health insurance to its customers and now they need to build a model to predict whether the policyholders (customers) from past year will also be interested in vehicle insurance. With the limited resources to contact the potential customers interested in vehicle insurance it is necessary to build a customers rank to enhance customer adhesion performance. This is a learning to rank project (LTR).</p>

<h3 dir="auto">Solution Proposal</h3>
<p>The solution of this problem consists in the use of a machine learning model to perform <strong>Learning to Rank</strong> task, i.e., create a sorted list with interested clients on the top from the original data.</p>

<h1 dir="auto">Solution methodology</h1>
<p>Focusing primarily in feedback agility, the solution will follow the CRISP methodology applied to data science, with the cycles being repeated as necessary.</p>

<p dir="auto"><strong>Step 01. Data Collection:&nbsp;</strong>The first step was to collect the data at a PostgreSQL database in the AWS Cloud and understand the data. There are 304887 customers records, containing different attributes such as: &quot;gender&quot;, &quot;age&quot;, &quot;driving license&quot;, &quot;vehicle age&quot;, &quot;policy sales channel&quot;, among others; these data show the customer&apos;s final interest in taking out car insurance, based on past experiences.</p>

<p dir="auto"><strong>Step 02. Data description:</strong> In this step we analyze if there are erroneous/missing data, data types and general information about the data who we will working.</p>

<p dir="auto"><strong>Step 03. Feature engineering:&nbsp;</strong>The responses of the &quot;vehicle age&quot; feature were changed to the snake_case pattern (for later one hot encoding) and the responses of the &quot;vehicle damage&quot; feature were also changed: the originals &quot;Yes&quot; and &quot;No&quot; by 1 and 0, respectively.</p>

<p dir="auto"><strong>Step 04. Data filtering:</strong> Soon after, the check for missing values and outliers took place.</p>

<p dir="auto"><strong>Step 05. Exploratory data analysis:&nbsp;</strong>The exploratory data analysis was carried out to bring up some relevant insights. Specific analyzes were also carried out to understand the influence of some features on the customer&apos;s final decision to acquire a vehicle insurance.</p>

<p dir="auto"><strong>Step 06. Data preparation:&nbsp;</strong>After analyzing the data, standard and minmax scalers were applied, in addition to target and frequency encoders for some features. All details are available on the notebook.</p>

<p dir="auto"><strong>Step 07. Feature selection:&nbsp;</strong>The next step was to identify the most relevant features for training machine learning models. In addition to the knowledge acquired during EDA, the Extra Tree algorithm was used. The features chosen by Extra Trees are described in the notebook.</p>

<p dir="auto"><strong>Step 08. Machine learning modelling</strong>: Different machine learning algorithms were evaluated and tested with cross-validation: random forest, knn, logistic regression, and extra trees. The &quot;predict_proba&quot; method (the probabilities for the target) was used to sort the customer&apos;s list and plot the cumulative gains and lift curves.</p>
<p dir="auto">Finally, <strong>precision@k</strong> and <strong>recall@k</strong> (in this case, k = 10%, 20%, 30% and 40%) metrics were used to quantify the performance of the models and to choose the better one.</p>
<ul dir="auto">
    <li>The <strong>precision@k</strong> counts how many predictions were correct up to k, and divides by all predictions made up to k.</li>
    <li>The <strong>recall@k</strong> counts how many predictions were correct up to k, and divides by all true examples.</li>
</ul>

<p dir="auto"><strong>Step 09. Convert model performance to business values:&nbsp;</strong>The manager was given an ordered list of customers most likely to purchase vehicle insurance. When contacting the top 40% of the list, it is expected that there will be a conversion of at least 86% of the total interested in the product.</p>

<h1 dir="auto">Top Three Data Insights </h1>
<h4 dir="auto">1) The owner of an older car is more likely to purchase a vehicle insurance</h4>
<table>
    <thead>
        <tr>
            <th>Vehicle age</th>
            <th align="center">Interested in vehicle insurance</th>
            <th align="center">Not interested in vehicle insurance</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Below 1 year</td>
            <td align="center">4.4%</td>
            <td align="center">95.6%</td>
        </tr>
        <tr>
            <td>Between 1 and 2 years</td>
            <td align="center">17.4%</td>
            <td align="center">82.6%</td>
        </tr>
        <tr>
            <td>Over 2 years</td>
            <td align="center">29.5%</td>
            <td align="center">70.5%</td>
        </tr>
    </tbody>
</table>

<h4 dir="auto">2) Customers with a previously damaged vehicle are more likely to purchase a vehicle insurance.</h4>
<img src=Images/vehicle_damage.png/>

<h4 dir="auto">3) Older customers are more likely to purchase a vehicle insurance</h4>
<img src=Images/age.png/>

<h1 dir="auto">Machine Learning Model Applied</h1>
<p>The ML model chosen to continue the analysis and calculate the predictions is the Linear Regression as this model had a good performance and requires less memory than the other models when deployed to production.</p>

<h2 dir="auto">Machine Learning Performance</h2>

<p>All machine learning algorithms were trained using cross validation on training data.</p>
<p dir="auto"><strong>Holdout Validation:</strong></p>
<table>
    <thead>
        <tr>
            <th align="center">Model</th>
            <th align="center">Precision</th>
            <th align="center">Recall</th>
            <th align="center">k%</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">random_forest</td>
            <td align="center">0.2741</td>
            <td align="center">0.8882</td>
            <td align="center">40.0</td>
        </tr>
        <tr>
            <td align="center">extra_trees</td>
            <td align="center">0.2713</td>
            <td align="center">0.8790</td>
            <td align="center">40.0</td>
        </tr>
        <tr>
            <td align="center">linear_regression</td>
            <td align="center">0.2666</td>
            <td align="center">0.8637</td>
            <td align="center">40.0</td>
        </tr>
        <tr>
            <td align="center">knn</td>
            <td align="center">0.2644</td>
            <td align="center">0.8567</td>
            <td align="center">40.0</td>
        </tr>
    </tbody>
</table>
<p dir="auto"><strong>Cross-validation:</strong></p>
<table>
    <thead>
        <tr>
            <th align="center">Model</th>
            <th align="center">k_folds</th>
            <th align="center">precision_avg</th>
            <th align="center">precision_std</th>
            <th align="center">recall_avg</th>
            <th align="center">recall_std</th>
            <th align="center">k%</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">random_forest</td>
            <td align="center">5</td>
            <td align="center">0.2734</td>
            <td align="center">0.0039</td>
            <td align="center">0.8922</td>
            <td align="center">0.0036</td>
            <td align="center">40.0</td>
        </tr>
        <tr>
            <td align="center">extra_trees</td>
            <td align="center">5</td>
            <td align="center">0.2697</td>
            <td align="center">0.0034</td>
            <td align="center">0.8798</td>
            <td align="center">0.003</td>
            <td align="center">40.0</td>
        </tr>
        <tr>
            <td align="center">linear_regression</td>
            <td align="center">5</td>
            <td align="center">0.2666</td>
            <td align="center">0.003</td>
            <td align="center">0.8702</td>
            <td align="center">0.0064</td>
            <td align="center">40.0</td>
        </tr>
        <tr>
            <td align="center">knn</td>
            <td align="center">5</td>
            <td align="center">0.2633</td>
            <td align="center">0.003</td>
            <td align="center">0.8594</td>
            <td align="center">0.0027</td>
            <td align="center">40.0</td>
        </tr>
    </tbody>
</table>

<h1 dir="auto">Business Results</h1>
<p>With the Machine Learning model adopted, the marketing team made call campaigns for ~90% of interested customers, reaching only 40% of the total customer base.

Assuming a cost per call of $10.00 and considering the total number of customers (381,109), the company achieved savings of $2,286,660 on phone calls costs (60% cost reduction).</p>


<h1 dir="auto">Conclusions</h1>
<p>With the use of the model in production, it is expected, at least, to double the efficiency in the acquisition of new clients for vehicle insurance.</p>

<p>This is because you will only need to contact 40% of customers to get around 90% conversion. Without the model, when contacting purely random customers, it is reasonable to say that to have 90% of customers likely to close a deal, you would also have to contact 90% of the total list.</p>

<h2 dir="auto">Next Steps</h2>
<ul>
<li><span class="VIiyi" lang="en"><span class="JLqJ4b ChMk0b" data-language-for-alternatives="en" data-language-to-translate-into="pt" data-phrase-index="0" data-number-of-phrases="5"><span class="Q4iAWc">Create more attributes from the existing ones, seeking to generate more inputs for learning the models.</span></span></span></li>
<li><span class="VIiyi" lang="en"> <span class="JLqJ4b ChMk0b" data-language-for-alternatives="en" data-language-to-translate-into="pt" data-phrase-index="2" data-number-of-phrases="5"><span class="Q4iAWc">Use more than one attribute selection method, including Boruta for example.</span></span> </span></li>
<li><span class="VIiyi" lang="en">Apply <span class="JLqJ4b ChMk0b" data-language-for-alternatives="en" data-language-to-translate-into="pt" data-phrase-index="4" data-number-of-phrases="5"><span class="Q4iAWc">hyperparameter fine tuning, in order to optimize the models.</span></span></span></li>
<li>Allow user to upload customer data as a csv file.</li>
<li>Display a dashboard on an application page with a brief exploratory analysis of the customer dataset used.</li>
</ul>
