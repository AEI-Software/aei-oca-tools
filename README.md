# AEI OCA Tools

Repositorio que centraliza los módulos de [OCA (Odoo Community Association)](https://github.com/OCA) utilizados en los despliegues de AEI Software.

## Módulos incluidos

| Módulo | Repositorio OCA | Rama | Commit |
|--------|-----------------|------|--------|
| `commission` | [OCA/commission](https://github.com/OCA/commission) | `17.0` | `5feb0df` |
| `helpdesk` | [OCA/helpdesk](https://github.com/OCA/helpdesk) | `17.0` | `0d5b353` |
| `project` | [OCA/project](https://github.com/OCA/project) | `17.0` | `b8924d0` |
| `timesheet` | [OCA/timesheet](https://github.com/OCA/timesheet) | `17.0` | `614cf06` |
| `web` | [OCA/web](https://github.com/OCA/web) | `17.0` | `5817d9d` |

## Actualizar un módulo

Cada subdirectorio conserva su repositorio Git interno, lo que permite actualizar directamente desde OCA:

```bash
# 1. Entrar al módulo y hacer pull
cd commission
git pull origin 17.0
cd ..

# 2. Ocultar temporalmente el .git interno para que el repo padre lo registre como archivos planos
mv commission/.git commission/.git_keep
git add commission
mv commission/.git_keep commission/.git

# 3. Commit del repo padre
git commit -m "[UPD] Actualizar commission desde OCA"
git push
```

## Notas

- Los archivos se almacenan como **contenido plano** (no como submódulos) para que al clonar el repositorio los archivos vengan completos.
- El directorio `venv/` está excluido del repositorio (`.gitignore`).
