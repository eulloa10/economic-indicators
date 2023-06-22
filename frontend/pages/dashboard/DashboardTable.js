import styles from '../../styles/Dashboard/DashboardTable.module.css';


function DashboardTable() {
  return (
    <div className={styles['dashboard-table']}>
      <div className={styles['dashboard-small-table']}>
        <ul className={styles['table-header']}>
          <li className={styles['table-header-column-names']}>
            Indicator
          </li>
          <li className={styles['table-header-column-names']}>
            Prior Period
          </li>
          <li className={styles['table-header-column-names']}>
            Current Period
          </li>
          <li className={styles['table-header-column-names']}>
            Delta
          </li>
        </ul>
      </div>
    </div>
  )
}

export default DashboardTable;
