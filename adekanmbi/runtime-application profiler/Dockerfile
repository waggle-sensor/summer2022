FROM waggle/plugin-base:1.1.1-ml-cuda10.2-l4t
#FROM ecpe4s/waggle-plugin-base:1.1.1-ml-cuda11.0-amd64
RUN apt update -y
RUN apt install -y gcc g++ zlib1g-dev autoconf automake make m4 libpython3.6-dev python3-dev wget
RUN wget http://tau.uoregon.edu/tau.tgz && tar -zxvf tau.tgz
WORKDIR /tau-2.31.1
RUN ./configure -bfd=download -python -pythonlib=/usr/lib/python3.6/config-3.6m-aarch64-linux-gnu -pythoninc=/usr/include/python3.6m -unwind=download -c++=g++ -cc=gcc
ENV PATH="/tau-2.31.1/arm64_linux/bin:$PATH"
RUN make -j4 install
ENV PYTHONPATH=/tau-2.31.1/arm64_linux/lib/bindings-python
COPY requirements.txt /app/
# RUN pip3 install --no-cache-dir -r /app/requirements.txt
COPY app.py live_metrics.py runtime_metrics.py thread.py start.sh firstprime.py /app/
COPY tegrastats /usr/bin/tegrastats
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1
RUN apt-get update && apt-get install -y vim
RUN pip install -U jetson-stats && python -m pip install psutil

# Install miniconda
# ENV CONDA_DIR /opt/conda
# RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
#      /bin/bash ~/miniconda.sh -b -p /opt/conda

# # Put conda in path so we can use conda activate
# ENV PATH=$CONDA_DIR/bin:$PATH

WORKDIR /app

# ENTRYPOINT ["/bin/bash"]
# CMD ["start.sh"]

# ENTRYPOINT ["python3", "/app/app.py"]
                                      