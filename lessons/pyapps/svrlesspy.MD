### Assignment
We will explore how to build an API-driven application
using Amazon API Gateway for serverless API hosting,
AWS Lambda for serverless compute,
and Amazon Cognito for serverless authentication.
We will follow an API-driven development process,
and first mock up what the API will look like.
We will cover all the ins and outs of the service
Amazon API Gateway.


And as you'll learn,
it does a lot more than just hosting an API.
Then we will add authentication to the API
using Amazon Cognito.
You'll learn about how the authorization flow
works with Cognito and how to build it into your APIs.
From there, we will add a Lambda backend
that will be triggered by API Gateway.
The Lambda functions that we will be using
will be using the AWS SDKs
to perform various data processing tasks.
You'll learn about the different configurations
that exist for Lambda,
and we will show you how to create
and manage Lambda functions.
Some of the features of our API
will require multiple Lambda functions
to execute in a specific order, like a workflow.
And we will be using AWS Step Functions
to create a serverless workflow.
Finally, we will talk about how to optimize your APIs
at every layer using AWS features.

Labs in this course follow a storyline where you are tasked with building out a website hosted on AWS using all serverless services. Each lab will walk you through building out the website and backend API step by step. The labs focus on the use of the AWS SDK and AWS CLI.

You will start by creating the front-end website, then the backend API, add authentication to that API, create the backend compute functions, create an asynchronous reporting workflow, and then implement distributed tracing, use monitoring features, and improving performance for the distributed application.

AWS services used: Amazon S3, Amazon API Gateway, Amazon Cognito, AWS Lambda, AWS Step Functions, AWS X-Ray, and Amazon Comprehend.

Lab 1: Create a static  Amazon S3 website with a bucket policy that restricts access to the website via IP Address. The website will be created using the AWS SDK and AWS CLI.

Lab 2: Setup mock backend API using Amazon API Gateway REST APIs. You will setup 3 API endpoints using the AWS SDK and AWS CLI, these endpoints will respond to requests with mocked data. You will test this mock API using the website setup in Lab 1 make AJAX calls to the mock API.

Lab 3: Secure the API that was built in Lab 2 by adding authentication via Amazon Cognito User Pools.

Lab 4: Create AWS Lambda functions to host the backend for your API. You will then configure the secured API built in Lab 3 to trigger to the lambda functions, instead of using mock integrations.

Lab 5: Create an asynchronous state machine using AWS Step Functions for a reporting feature of the API. You will then configure the API to run this state machine when a request hits an API endpoint you built in the previous labs.

Lab 6: Use AWS X-Ray to trace requests through your distributed application. You will also make improvements to your application using various AWS service features like Amazon API Gateway Response Caching, as well as code modifications. Then you will test and view the performance improvements in the AWS X-Ray Console.


Note: Verified students have access to hands-on lab exercises. Students auditing the class have access to the lectures, readings, and discussion groups. Hands-on exercises will be run in a lab environment directly from the class.  There is no additional cost for paid students.


Now, for various security and design reasons
you generally don't want to expose your data
directly to your consumers.
Instead, you want to expose your data to your consumers
via an API, or application programming interface.
We don't want to allow people to query the data
from our S3 bucket directly.
Instead, we are going to build out an API
using Amazon API Gateway to expose that data securely.

AWS APIs
Everything in AWS is an API call and every AWS Service has its own set of APIs that you interact with. When you send HTTP requests to AWS, you sign the requests so that AWS can identify who sent them. You sign requests with your AWS access key, which consists of an access key ID and secret access key. You need to sign HTTP requests only when you manually create them. When you use the AWS Command Line Interface (AWS CLI) or one of the AWS SDKs to send requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

To read about how requests need to be signed, click here: https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html

AWS Command Line Interface
The AWS Command Line Interface (AWS CLI) is an open source tool that enables you to interact with AWS services using commands in your command-line shell.

Installation of the AWS Command Line Interface is fairly straightforward, and if you’re using Amazon EC2 instances or AWS Cloud9, the tools are already installed for you.

After configuration, the AWS CLI enables you to start running commands that implement functionality equivalent to that provided by the browser-based AWS Management Console from the command prompt in your favorite terminal program:

Linux shells – Use common shell programs such as bash, zsh, and tcsh to run commands in Linux or macOS.

Windows command line – On Windows, run commands at the Windows command prompt or in PowerShell.

Remotely – Run commands on Amazon Elastic Compute Cloud (Amazon EC2) instances through a remote terminal program such as PuTTY or SSH, or with AWS Systems Manager.

Read information about the AWS CLI at: https://aws.amazon.com/cli/

Read information about installing the AWS CLI at: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html

Read information about configuring the AWS CLI at: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

AWS Cloud9
AWS Cloud9 operates as a cloud-based IDE, and has a wide variety of functionality already built in to help you with the development of and collaboration on your projects. A particular area where Cloud9 can assist is when working with the AWS Command Line Interface. Because the CLI tools are already installed in your environment, all you need to do is configure them to get started.

You access the AWS Cloud9 IDE through a web browser. You can configure the IDE to your preferences. You can switch color themes, bind shortcut keys, enable programming language-specific syntax coloring and code formatting, and more.

Read more about Cloud9 at: https://docs.aws.amazon.com/cloud9/latest/user-guide/welcome.html

AWS Cloud9 managed temporary credentials have permission restrictions on their own which may restrict some API calls you are using. You can find the list of those restrictions at:

https://docs.aws.amazon.com/cloud9/latest/user-guide/auth-and-access-control.html#auth-and-access-control-temporary-managed-credentials-supported

AWS Credentials and Programmatic Access
Read about best practices with AWS Credentials here: https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html