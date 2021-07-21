{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled13.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPl7z+g39v8mv3VIXRwen1v",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/miguelcapera2011/ADSI/blob/main/lista_comprension.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E-uq_IjJTiMT",
        "outputId": "2ba0752e-19a5-49df-ca80-17e49ddcf0a1"
      },
      "source": [
        "\"\"\"Apartir de la libreria random obtener numeros enteros y asignarlos a una lista vacia,los cuales se recorreran y \n",
        "por medio de una condicion, tendras que identificar si son pares o impares dentro de la misma lista(usar lista por comprension)\"\"\"\n",
        "\n",
        "\n",
        "import random #importamos la libreria random\n",
        "listaElementosAleatorios=[]#se crea una lista  vacia\n",
        " \n",
        "for _ in range(1,5):#se usa un bucle for para obtener los  elementos que haran parte de la lista vacia\n",
        "    numeroAleatorio=random.randint(1,40)#en una variable guardamos los valores aleatorios que itera el bucle,en total 4\n",
        "    listaElementosAleatorios.append(numeroAleatorio)#el metodo append Agrega un ítem al final de la lista,Extiende la lista agregándole todos los ítems del iterable. \n",
        "    result = [f\"{i} es par\" if i%2==0 else f\"{i} es impar\" for i  in listaElementosAleatorios]#a una variable se guarda una lista por comprension\n",
        "    \n",
        "print(listaElementosAleatorios)#se muestra la lista para si compararla con el resultado de elementos\n",
        "print(result)#resultado\n",
        " \n"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[34, 9, 40, 3]\n",
            "['34 es par', '9 es impar', '40 es par', '3 es impar']\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}