#!/bin/bash

# Définition du nom de l'environnement
ENV_NAME="bbs"

# 🔹 Étape 1: Suppression de l'ancien environnement s'il existe
if conda info --envs | grep -q "^$ENV_NAME\s"; then
    echo "🔄 Suppression de l'environnement existant: $ENV_NAME"
    conda deactivate 2>/dev/null  # Désactiver l'environnement s'il est actif
    conda env remove --name $ENV_NAME -y -q
    echo "✅ Environnement $ENV_NAME supprimé avec succès."
fi

# 🔹 Étape 2: Création d'un nouvel environnement Conda
echo "🚀 Création du nouvel environnement: $ENV_NAME"
conda create --name $ENV_NAME python=3.12 ipykernel -y

# 🔹 Étape 3: Activation du nouvel environnement
echo "🟢 Activation de l'environnement: $ENV_NAME"
eval "$(conda shell.bash hook)"
conda activate $ENV_NAME
conda config --set channel_priority flexible

# 🔹 Étape 4: Installation de GCC pour la compilation
echo "🛠️ Installation de GCC 12..."
conda install -c conda-forge gcc=12 -y

# 🔹 Étape 5: Installation de CUDA et cuDNN pour GPU
echo "⚡ Installation de CUDA Toolkit et cuDNN..."
conda install -c nvidia cudatoolkit=11.8.0 cudnn=8.9.7 -y

# 🔹 Étape 6: Installation de PyTorch et des dépendances CUDA
echo "🔥 Installation de PyTorch et des bibliothèques associées..."
conda install -c pytorch -c nvidia pytorch=2.5.1 torchvision=0.20.1 torchaudio=2.5.1 pytorch-cuda="11.8" -y

# 🔹 Étape 7: Installation des bibliothèques ML/NLP
echo "📚 Installation des bibliothèques ML/NLP..."
conda install -c conda-forge -c nvidia tensorflow=2.14.0 -y
conda install -c conda-forge transformers=4.49.0 -y
conda install -c conda-forge ipywidgets -y  
conda install -c conda-forge scikit-learn=1.6.1 -y 
conda install -c conda-forge tiktoken=0.9.0 -y 

# 🔹 Étape 8: Installation des paquets supplémentaires via pip
echo "🌐 Installation des bibliothèques Langchain et AI supplémentaires..."

echo "Filtering Conda-only packages. This may take some time..."
# Loop through each package in the requirements file
output_file="conda_requirements.txt"; > "$output_file"
# conda list | awk 'NR>3 && $4 != "" {print $1 "==" $2}' | sed '/^#/d' | sed '/^__pip/d' | xargs -P 10 -I {} bash -c '
#     package=$(awk -F "==" "{print \$1}" <<< "{}");
#     version=$(awk -F "==" "{print \$2}" <<< "{}");
#     # Check if package exists on PyPI
#     if pip index versions "$package" &>/dev/null; then
#         echo "$package==$version"
#     fi
# ' >> "$output_file";
cat > "$output_file" <<EOF
torch==2.5.1
torchvision==0.20.1
torchaudio==2.5.1
scikit-learn==1.6.1
tiktoken==0.9.0
transformers==4.49.0
# tensorflow==2.14.0
EOF
python -m pip install --no-cache-dir -r conda_requirements.txt \
    langchain==0.3.20 langchain-community==0.3.19 langgraph==0.3.5 \
    langchain_experimental==0.3.4 langchain-nomic==0.1.4 langchain-openai==0.3.8 \
    langchain-ollama==0.2.3 langchain-chroma==0.2.2 \
    sentence_transformers==3.4.1 spacy==3.8.4 duckduckgo-search==7.5.1 \
    "pypdf[full]==5.3.1" faiss-gpu-cu11==1.10.0 chromadb==0.6.3 open_clip_torch==2.31.0 \
    "nomic[local]==3.4.1" wikipedia==1.4.0
python -m spacy download fr_core_news_sm

# 🔹 Étape 9: Télécharge les fichiers externes utilisés par le notebook
wget -q -O demo1.webp https://raw.githubusercontent.com/P2Enjoy/academy-tutorial-python/main/rag/rag/demo1.webp
wget -q -O demo2.png https://raw.githubusercontent.com/P2Enjoy/academy-tutorial-python/main/rag/rag/demo2.png
wget -q -O LangraphStudioProxy.py https://raw.githubusercontent.com/P2Enjoy/academy-tutorial-python/refs/heads/main/rag/rag/LangraphStudioProxy.py
wget -q -O config.env https://raw.githubusercontent.com/P2Enjoy/academy-tutorial-python/refs/heads/main/rag/rag/config.env.exemple

# 🔹 Étape A: Add the conda environment to the user kernels
if jupyter kernelspec list | grep -q "$ENV_NAME"; then
    echo "Kernel '$ENV_NAME' exists. Removing it..."
    jupyter kernelspec remove -f "$ENV_NAME"
fi
python -m ipykernel install --user --name $ENV_NAME --display-name "BBS"

echo "✅ Installation complète de l'environnement $ENV_NAME ! 🚀"
