![Capture](https://res.cloudinary.com/dhhax6yae/image/upload/v1692449705/Screenshot_2023-08-19_at_6.01.09_PM_jykedv.png)

# Guardian
---

`Guardian` is a cutting-edge solution designed to revolutionize the way organizations approach security compliance monitoring and remediation. In today's rapidly evolving digital landscape, maintaining adherence to security policies, standards, and baselines is paramount. However, the manual assessment of logs, system configurations, access controls, and user privileges can be a time-consuming and error-prone process.

`Guardian` addresses these challenges by leveraging the power of large language models to automate the identification of non-compliant activities and provide actionable insights for effective remediation.

Contents
---

* [Installation](#installation)
* [Tech-Stacks Used](#tech-stacks-used)
* [Features Added](#use-cases)
* [Future Scope](#future-scope)
* [Snapshots](#snapshots)
* [Deployed Link](#deployed-link)

### Installation:
---
#### Setup Virtual Environment

To ensure a clean and isolated environment for your application, it's recommended to use a virtual environment. Here's how you can set it up:

```
cd {your-repo}
python -m virtualenv venv
```
Activating the Virtual Environment
- On Windows:
```
venv\Scripts\activate
```

- On macOS and Linux:

```
source venv/bin/activate
```

#### Install Dependencies
With the virtual environment activated, install the required dependencies using pip and the requirements.txt file:
```
pip install -r requirements.txt
```
#### Setup .env
To run the LLM we need to create a .env file and add our openai api key to it 

```
OPENAI_API_KEY = "{your_api_key}"
```

#### Start the Application
Navigate to the "Flipkart_Security" directory, which contains the application code:
```
cd Flipkart_Security
```

Run the following command to start the application:
```
python manage.py runserver
```

#### Access the Application
Open your web browser and go to http://127.0.0.1:8000/ 

### Tech-Stacks Used:
---

- Python
- LangChain
- OpenAI
- Django
- Javascript
- Azure


### Use Cases
---
<ol>
<li>Security Compliance Monitoring:
To monitor and ensure adherence to security policies, standards, and baselines. The system can analyze logs, system configurations, access controls, and user privileges to identify any non-compliant activities that might violate security protocols.</li></br>
<li>Audit and Reporting:
The solution can provide automated auditing capabilities by analyzing logs and generating detailed compliance reports. This can be valuable for internal auditing purposes as well as for presenting compliance status to regulatory bodies or stakeholders.
</li></br>
<li>Automated Remediation:
Alongside identifying compliance breaches, the system can provide actionable insights on how to remediate the issues. This includes suggesting specific configuration changes, access control adjustments, and policy updates.
</li></br>
<li>Cross-Platform Compliance:
With the flexibility to handle various log formats and compliance standards, the solution can be applied across different systems and environments, ensuring consistency in compliance monitoring.
</li></br>
</ol>

--------
### Deployed Link 
---

[Deployed Link](http://52.255.177.160)
[Deployed Video](https://drive.google.com/file/d/10bg293V7i0WMPWPftFM3b8gGsHPIXGL1/view?usp=drive_link)

# Note 
- Due to resource constraints, we have used OpenAI models, We believe we can produce similar results if we have access to computational resources.
