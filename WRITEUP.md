# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.


Analyze, choose, and justify the appropriate resource option for deploying the app.

Virtual Machines (VMs)
Costs: VMs typically have a higher cost because you pay for the OS licensing and the physical resources allocated, regardless of usage. So I also incur costs related to the management and maintenance of the OS and server software.

Scalability: Scaling VMs can be more complex and slower because it often involves manual configuration, adding new VM instances, and balancing load among them.

Availability: High availability can be achieved but requires careful setup like Availability Sets or Zones, Load Balancers, and auto-scaling configurations, which add complexity.

Workflow: Integrating development workflows (CI/CD) with VMs involves additional steps such as scripting deployments and managing updates to server configurations and applications.

Azure App Service
Costs: Generally more cost-effective for web apps due to the abstraction of underlying infrastructure. I can pay based on the plan which can scale in terms of capabilities and cost depending on demand.

Scalability: Easier and quicker to scale horizontally or vertically with just a few clicks in the management portal or via automated rules set based on performance metrics.

Availability: Built-in high availability. Azure handles hardware failures, network issues, and distributes across fault domains.

Workflow: Native integration with Azure DevOps, GitHub, and other CI/CD tools for continuous deployment, along with various developer tools and extensions.

Decision and Justification
Given the requirements of a CMS application, which typically needs reliable scalability, moderate to high availability, and a streamlined deployment process, Azure App Service is the more appropriate choice. It offers:

Simplified Management: Automated management, patching, and scaling.
Cost Efficiency: More predictable costs without the overhead of managing physical servers or virtual machines.
Integrated Services: Easy integration with other Azure services like SQL Database, Azure Active Directory, and more.
Developer-Friendly: Supports quick setups and is conducive to agile development practices.
Azure App Service abstracts much of the infrastructure management required by VMs, allowing developers to focus on application development rather than server maintenance. This will reduce the operational burden and streamline workflow processes.

Assess app changes that would change your decision
Changes in the application or business requirements could lead us to reconsider the decision to use Azure App Service. Such changes might include: