import { useEffect } from 'react';
import styles from '../../styles/Dashboard/DashboardTable.module.css';

function DashboardTable({ data }) {
  console.log('data :>> ', data);

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

export const getStaticProps = async () => {
  const response = await fetch('localhost:8000/api/indicators/yield_curve');
  const data = await response.json();
  console.log('DATAPROPS :>> ', data);
  console.log('ENTERED')

  return {
    props: {
      data
    }
  }
}

export default DashboardTable;
