import { useEffect } from 'react';
import styles from '../../styles/Dashboard/DashboardTable.module.css';

async function getIndicators() {
  const res = await fetch('/api/reports/recent')
  return res.json()
}

function DashboardTable() {
  let indicatorData = {}

  useEffect(() => {
    indicatorData = getIndicators();
  }, [indicatorData]);

  console.log("INDICATORDATA", indicatorData)

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
