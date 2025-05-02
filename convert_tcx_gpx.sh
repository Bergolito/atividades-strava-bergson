#!/bin/bash

# Define os diretórios de entrada e saída
INPUT_DIR="INPUT"
OUTPUT_DIR="OUTPUT"

# Verifica se o diretório de entrada existe
if [ ! -d "$INPUT_DIR" ]; then
  echo "Erro: O diretório de entrada '$INPUT_DIR' não existe."
  exit 1
fi

# Cria o diretório de saída se não existir
mkdir -p "$OUTPUT_DIR"

# Encontra todos os arquivos .tcx no diretório de entrada e itera sobre eles
find "$INPUT_DIR" -name "*.tcx" -print0 | while IFS= read -r -d $'\0' tcx_file; do
  # Extrai o nome base do arquivo TCX para criar o nome do arquivo GPX
  base_name=$(basename "$tcx_file" .tcx)
  gpx_file="$OUTPUT_DIR/${base_name}.gpx"

  # Converte o arquivo TCX para GPX usando gpsbabel
  echo "Convertendo '$tcx_file' para '$gpx_file'..."
  gpsbabel -i tcx -f "$tcx_file" -o gpx -F "$gpx_file"

  # Verifica se a conversão foi bem-sucedida (opcional)
  if [ $? -eq 0 ]; then
    echo "Conversão bem-sucedida."
  else
    echo "Erro durante a conversão de '$tcx_file'."
  fi
done

echo "Processo de conversão concluído."