# Git y GitHub

## Clonar repositorios

```bash
git clone https://github.com/12aptor/data-science-g4.git
```

## Descargar información del repositorio

```bash
git fetch
```

## Descargar cambios del repositorio

```bash
git pull origin nombre_rama
```

## Subir cambios al repositorio

```bash
git add nombre_archivo
git commit -m "mensaje"
git push origin nombre_rama
```

## Cambiar de rama

```bash
git switch nombre_rama
```

#git add .: Este comando se usa para preparar los cambios (archivos nuevos, modificados o eliminados) para ser guardados. El . significa que añades todos los cambios en el directorio actual y sus subdirectorios.

git commit -m "git y github": Este comando guarda los cambios que preparaste con git add. El -m te permite añadir un mensaje descriptivo (en este caso, "git y github") que explica qué cambios realizaste en este commit. Es como tomar una "instantánea" de tu proyecto.

git push origin modulo1: Después de haber guardado los cambios localmente con git commit, este comando los envía al repositorio remoto. origin es el nombre predeterminado que se le da al repositorio remoto principal (generalmente en GitHub), y modulo1 es el nombre de la rama en la que estás trabajando y cuyos cambios quieres subir.
