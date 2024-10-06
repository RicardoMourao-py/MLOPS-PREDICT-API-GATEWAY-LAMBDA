FROM public.ecr.aws/lambda/python:3.10

# Copy requirements.txt
COPY . ${LAMBDA_TASK_ROOT}

# Install system dependencies, ignoring SSL certificate errors
RUN yum install -y --nogpgcheck libstdc++ cmake gcc-c++ || \
    yum install -y --setopt=sslverify=false libstdc++ cmake gcc-c++ && \
    yum clean all && \
    rm -rf /var/cache/yum

# Install the specified packages
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "main.main" ]