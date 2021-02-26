Automate data processing in a data source
====================================================

Data sources are systems your company uses to store and process customer data.

Adding a data source allows you to automate interaction with it while processing data subject requests.

In other words, you won't have process data manually in each data source. Soveren Privacy Suite will do it for you.

------------

Soveren distinguishes between standard and custom data sources:

* A standard data source is normally a SaaS system, such as Mailgun, HubSpot, ZenDesk, etc.

* A custom data source is normally an on-premise company solution for storing data, such as a relational database like MySQL or PostgreSQL.

Once you added a data source, you can automate data processing with it.

.. tab:: Automate a data source

   1. Automate interaction with the source by connecting to the source one of the following ways:

      * Via OAuth 2.0:

        1. Click **Connect** to be redirected to the source.

        2. Sign in to your account in the source.

        3. Allow Soveren access to the source.

      * Via an API key:

        1. On the page **Automation** tab, click **Read how to find the source API key** and read the instruction.

        2. Follow the instruction from #1 and copy the API key.

        3. Paste the API key to they field **API key** on the **Automation** tab.

   2. Enable automation of data processing for the source.

      Use the **Automation** toggle from the **Automate data processing** section.

   .. tip::

      The **Automation** toggle only enabled or disables automation in general.

      You still need to enable automation for specific request types below.

   3. Enable automation of data processing per subject request type.

      Use the toggles from the **Control automation by type** section.

   .. tip::

      The toggles from the **Automate data processing** section only apply when the **Automation** toggle is on.

.. tab:: Automate a custom data source

   To automate a custom data source:

   1. Contact us at support@soveren.io to request a questionnaire.

   2. Pass your engineering team the questionnaire to outline the necessary technical details.

   3. Send us the filled out questionnaire to support@soveren.io.

   4. Wait till we contact you and arrange a timeslot to deploy an instance of Soveren agent for your company and set up conection between the agant and your Soveren account.

   5. Enable automation of data processing for the source.

      Use the **Automation** toggle from the **Automate data processing** section.

   .. tip::

      The **Automation** toggle only enabled or disables automation in general.

      You still need to enable automation for specific request types below.

   6. Enable automation of data processing per subject request type.

      Use the toggles from the **Control automation by type** section.

   .. tip::

      The toggles from the **Automate data processing** section only apply when the **Automation** toggle is on.
















