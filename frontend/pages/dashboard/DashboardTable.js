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
            Current Period (CP)
          </li>
          <li className={styles['table-header-column-names']}>
            Prior Period (PP)
          </li>
          <li className={styles['table-header-column-names']}>
            CP Value
          </li>
          <li className={styles['table-header-column-names']}>
            PP Value
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
