---
fullname: Jorge Barata
address: Madrid, Spain
title: Full Stack Software Engineer

phone: 34 619 98 15 38
mail: contact@jorgebg.com
github: github.com/jorgebg
linkedin: linkedin.com/in/baratajorge
stackoverflow: stackoverflow.com/u/959819
home: jorgebg.com
pdffile: Jorge Barata.pdf

preferences: Full Stack, Django, React, Reliability, Machine Learning, GNU/Linux
---

# Summary

**Software Engineer** with 15 years of experience, the majority spent working on **large-scale applications**. Expertise in **backend** development with _Python_, _Django_, and relational databases. Proficient in **site reliability** and **infrastructure** with _Ansible_, _Terraform_, _AWS_. Experienced in **frontend** with _React_ and _TypeScript_, **machine learning** with _Scipy_ and _scikit-learn_, and **big data** with _Spark_.

Strong **software design** skills: OOP, TDD, DDD, SOA, clean architecture. Looking forward to developing a career as **Software Architect**, having gathered extensive knowledge in integrating a broad range of state-of-the-art patterns and technologies.

Active **free and open-source software** contributor and speaker.

# Experience

## Senior Software Engineer

> September 2018 -- December 2022 ◦ _Eventbrite , Madrid_

- Eventbrite is the market leader for live event ticketing globally. The platform handles hundreds of thousands of requests during the on-sales.
- Worked in a fast paced agile environment with distributed teams in different locations and time zones.
- Leaded the following projects:
  - Migration of a Django+PySOA service to a Kotlin+gRPC service. Zero downtime using traffic shadowing and incremental rollout. This resolved existing performance bottlenecks and streamlined the communication across the services in our SOA model.
  - Migration of a Redis-backed Django service to ElastiCache, reducing operational overhead and enhancing reliability and scalability.
  - Migration of parts of the monolith to SOA services in Django+PySOA, facilitating independent development and scalability.
  - Conducted Python and Django training sessions for engineering teams, enhancing the onboarding process by accelerating new hires' productivity and integration into projects, as most of our services were built in Django.
- Added new features to the event listing page and ticket order page, which improved the sales funnel.
- Joined the SRE team for some time, where I worked on the following projects:
  - Migration from in-house infrastructure management system to Terraform and CloudFormation, enabling efficient provisioning and consistent configurations across environments.
  - Trained the teams to set up Datadog dashboards, monitoring alerts, SLAs and error budgets, which allowed them to measure performance and improve the reliability.
- Conducted over a hundred interviews and delivered many talks in tech events, playing a pivotal role in talent acquisition and knowledge dissemination, enriching our team with diverse talents and fostering industry connections.
- Founded and organized the Django Madrid User Group, and Eventbrite sponsored the meetups. This brought more candidates to the hiring pipeline.
- Stack:
  - Backend: Django, Django REST Framework, Celery, MySQL, Redis, Elastic Search, PySOA, Varnish, RabbitMQ.
  - Frontend: React, TypeScript.
  - Infrastructure: Docker, uWSGI, HashiCorp (Consul, Nomad, Terraform), AWS (Fargate, DynamoDB, ElastiCache, CloudFormation), NGINX, HAProxy, Ubuntu, GitHub, Datadog, Sentry.
- https://eventbrite.com https://github.com/eventbrite/pysoa

## Senior Software Engineer

> July 2015 -- August 2018 ◦ _Udemy , Dublin_

- Udemy for Business (UFB) team. We created a platform with 20k+ courses offering on-demand, immersive, and cohort-based learning for businesses.
- Worked in a fast paced agile environment with distributed teams in different locations and time zones.
- Leaded the following projects:
  - Hierarchical taxonomy management system for the course collection. It allowed the customers to organize the courses and increased adoption.
  - Refactoring of the UFB's search system, moving from a dedicated implementation to a shared solution for the whole organization, which improved the team speed for developing experiments, new features, and the adoption from external developments.
  - Enriched the course search by adding related lectures, which resulted on more search clicks and course consumption.
  - A RESTful public API, enabling customers integration to the platform.
  - Instrumentalization to monitor the quality of the delivery, alarms that notified the team on fortuitous behaviours.
- Developed a self-service system that allowed customers to create learning portals for small teams. This helped to acommodate a market that today represents an important share of the current business.
- Migrated old code to new stacks:
  - From a in-house PHP framework to Django. This improved the onboarding learning curve.
  - From Angular 1 to React+MobX, which gave us more flexibility.
- Developed data pipelines for UFB analytics in AWS Redshift, Pinball, Python and ChartIO.
- 3rd party services integration: Intercom, Slack, Marketo, PingOne/PingFederate.
- Stack:
  - Backend: Django, Django Rest Framework, Celery, MySQL, Memcached, Redis, Elastic Search.
  - Frontend: React, MobX, Webpack, Babel, Karma.
  - Infrastructure: Docker, uWSGI, Fabric, Ansible, CentOS, GitHub, Jenkins, Datadog.
- http://udemy.com http://business.udemy.com

## Co-founder & CTO

> November 2016 -- September 2024 ◦ _Cooperativa Social Los Mochuelos , Madrid_

- Leaded the development and launch of the _Reutiliza_ project, a place for exchange and reuse of items. Built in Django and PostgreSQL and deployed on Debian with uWSGI, Nginx and Ansible.
- Technology advisor for all the projects of the cooperative, as well as system management and software development. Wordpress multi-site, infrastructure, networking, and office suite.
- http://mochuelos.com http://reutilizabocema.com

## Co-founder & CTO

> June 2014 -- November 2014 ◦ _Indievelopment, Dublin_

- Indievelopment, a LaunchBox 2015 startup (Trinity College's accelerator for student startups).
- Designed a crowdfunding platform for indie video games, deployable on Microsoft Azure.
- http://indievelopment.info http://launchbox.ie/companies/indievelopment https://www.f6s.com/indievelopment

## Software Engineer

> September 2012 -- June 2014 ◦ _Vivocom EU, Madrid_

- Extended the web application architecture (Yii+MySQL) with MongoDB, caching, background workers and querying, automation tools (Grunt), TDD, code quality linter, web security pentesting. Leaded the frontend implementation with CoffeeScript, CommonJS and Bower. Also trained the team for these new technologies/paradigms.
- Software design with ArgoUML, Continuous Integration with Github, Agile development with Kanban/Scrum/Redmine
- Server side performance optimization with PHPcache. Database query optimization of MySQL/MongoDB.
- Built a real time chat for the website: Integrated an Ejjaberd chat server with a WSDL DaaS. Web client built in Ember.js.
- 100,000 registered users in its first year. Funded by the Spanish Ministry of Industry, Energy and Tourism as part of _Plan Avanza 2_ program. It was awarded the Prize for Most innovative business project by the _Inspirational Festival_ of 2013.
- http://keepunto.com http://youtu.be/usjou9iFj7U http://planavanza.es http://inspirationalfestival.com

# Education

## B.Sc. Computer Engineering, \\\ M.Sc Distributed Systems

> August 2007 -- August 2017 ◦ _Universidad Carlos III de Madrid_

- **Taxi Recommendation System for Big Data**: Final dissertation. It consisted of two parts:

  - Data pipeline built in SciPy, scikit-learn, and Spark and deployed in the laboratory cluster.
  - Web application with geospatial features built in Django and PostGIS.

- https://github.com/jorgebg/taxi-recommendation-system

## M.Sc Teacher Training

> September 2023 -- October 2024 ◦ _Universidad Europea, Madrid_

## Languages

- **Spanish**: native
- **English**: fluent (4 years working in Ireland, C1)

---

## Additional Information

- Formar founder and organizer of **Madrid Django User Group**. https://www.meetup.com/MadridDjango/
- Former founder and organizer of **Dublin Django User Group**. https://www.meetup.com/django-dublin/
- Imparted a Django web framework course at the IE University.
- Over a dozen of tech talks. https://jorgebg.com/talks/
- Contributed to OSS projects: **Django**, **Yii**, **Symfony**, along others. https://github.com/jorgebg
- Please refer to my LinkedIn profile for previous work experience. https://linkedin.com/in/baratajorge
