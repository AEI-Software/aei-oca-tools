# AEI OCA Tools — Odoo 18.0

Repositorio que centraliza los módulos de [OCA (Odoo Community Association)](https://github.com/OCA) utilizados en los despliegues de AEI Software.

**Rama:** `18.0`

## Módulos incluidos

| Módulo | Repositorio OCA | Rama | Commit |
|--------|-----------------|------|--------|
| `account-reconcile` | [OCA/account-reconcile](https://github.com/OCA/account-reconcile) | `18.0` | `61b1aa1` |
| `commission` | [OCA/commission](https://github.com/OCA/commission) | `18.0` | `f0da6df` |
| `helpdesk` | [OCA/helpdesk](https://github.com/OCA/helpdesk) | `18.0` | `cf04d92` |
| `project` | [OCA/project](https://github.com/OCA/project) | `18.0` | `c8be550` |
| `timesheet` | [OCA/timesheet](https://github.com/OCA/timesheet) | `18.0` | `8910c51` |
| `web` | [OCA/web](https://github.com/OCA/web) | `18.0` | `fedf87bf` |

## Actualizar un módulo

Cada subdirectorio conserva su repositorio Git interno, lo que permite actualizar directamente desde OCA:

```bash
# 1. Entrar al módulo y hacer pull
cd commission
git pull origin 18.0
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
