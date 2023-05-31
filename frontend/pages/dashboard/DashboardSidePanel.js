import styles from '../../styles/Dashboard/DashboardSidePanel.module.css';

import MonthFilter from './MonthFilter';

function DashboardSidePanel() {
  return (
    <div className={styles['dashboard-inner-container']}>
      <MonthFilter />
    </div>
  )
}

export default DashboardSidePanel;
