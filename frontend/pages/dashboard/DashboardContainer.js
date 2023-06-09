import styles from '../../styles/Dashboard/DashboardContainer.module.css';

import DashboardSidePanel from './DashboardSidePanel';
import DashboardTable from './DashboardTable';

function DashboardContainer({data}) {
  return (
    <div className={styles['dashboard-container']}>
      <DashboardSidePanel />
      <DashboardTable data={data} />
    </div>
  )
}

export default DashboardContainer;
