import styles from '../../styles/Dashboard/DashboardContainer.module.css';

import DashboardSidePanel from './DashboardSidePanel';
import DashboardTable from './DashboardTable';

function DashboardContainer() {
  return (
    <div className={styles['dashboard-container']}>
      <DashboardSidePanel />
      <DashboardTable />
    </div>
  )
}

export default DashboardContainer;
