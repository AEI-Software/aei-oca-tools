# AEI OCA Tools — Odoo 19.0

Repositorio que centraliza los módulos de [OCA (Odoo Community Association)](https://github.com/OCA) utilizados en los despliegues de AEI Software.

**Rama:** `19.0`

## Módulos incluidos

| Módulo | Repositorio OCA | Rama | Commit |
|--------|-----------------|------|--------|
| `account-reconcile` | [OCA/account-reconcile](https://github.com/OCA/account-reconcile) | `19.0` | `a9bbab6` |
| `commission` | [OCA/commission](https://github.com/OCA/commission) | `19.0` | `cc2f1cf` |
| `helpdesk` | [OCA/helpdesk](https://github.com/OCA/helpdesk) | `19.0` | `2dc05a4` |
| `project` | [OCA/project](https://github.com/OCA/project) | `19.0` | `7f451fe` |
| `timesheet` | [OCA/timesheet](https://github.com/OCA/timesheet) | `19.0` | `c896dfe` |
| `web` | [OCA/web](https://github.com/OCA/web) | `19.0` | `01b0592` |

## Actualizar un módulo

Cada subdirectorio conserva su repositorio Git interno, lo que permite actualizar directamente desde OCA:

```bash
# 1. Entrar al módulo y hacer pull
cd commission
git pull origin 19.0
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
