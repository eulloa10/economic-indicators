import styles from '../../styles/Dashboard/DashboardSidePanel.module.css';

import MonthFilter from './MonthFilter';
import IndicatorFilter from './IndicatorFilter';
import UpdateButton from './UpdateButton';
import ScheduleReportButton from './ScheduleReportButton';

function DashboardSidePanel() {
  return (
    <div className={styles['dashboard-inner-container']}>
      <MonthFilter />
      <IndicatorFilter />
      <UpdateButton />
      <ScheduleReportButton />
    </div>
  )
}

export default DashboardSidePanel;
