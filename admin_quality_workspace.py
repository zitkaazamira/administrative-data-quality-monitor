
import random
from datetime import datetime, timedelta

import pandas as pd
import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Administrative Data Quality Monitor",
    page_icon="🌷",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# GLOBAL STYLE
# =========================================================

st.html(
    """
    <style>
        :root {
            --ink: #3d2f38;
            --muted: #7f6d77;
            --rose: #d97f9e;
            --berry: #9c5578;
            --lavender: #d9c9ef;
            --peach: #f6cbb8;
            --cream: #fffaf7;
            --line: #eadfe4;
        }

        .stApp {
            background:
                radial-gradient(
                    circle at 8% 7%,
                    rgba(246, 203, 184, 0.44),
                    transparent 24%
                ),
                radial-gradient(
                    circle at 91% 10%,
                    rgba(217, 201, 239, 0.48),
                    transparent 24%
                ),
                radial-gradient(
                    circle at 85% 78%,
                    rgba(217, 127, 158, 0.18),
                    transparent 23%
                ),
                linear-gradient(
                    180deg,
                    #fffdfc 0%,
                    #fff7fa 50%,
                    #fffaf7 100%
                );
        }

        .block-container {
            max-width: 1240px;
            padding-top: 5.1rem;
            padding-bottom: 4rem;
        }

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        div.stButton > button,
        div.stDownloadButton > button {
            min-height: 46px;
            border: none;
            border-radius: 14px;
            color: white;
            font-weight: 700;
            background:
                linear-gradient(
                    135deg,
                    #8d4a6b,
                    #c4698b
                );
            box-shadow:
                0 8px 20px rgba(141, 74, 107, 0.20);
        }

        div.stButton > button:hover,
        div.stDownloadButton > button:hover {
            color: white;
            border: none;
            background:
                linear-gradient(
                    135deg,
                    #7c3f5d,
                    #ad5779
                );
        }

        div[data-testid="stDataFrame"] {
            border: 1px solid var(--line);
            border-radius: 18px;
            overflow: hidden;
            box-shadow:
                0 8px 22px rgba(105, 63, 82, 0.055);
            background: white;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 0.4rem;
            padding: 0.35rem;
            border: 1px solid var(--line);
            border-radius: 15px;
            background: rgba(255,255,255,0.70);
        }

        .stTabs [data-baseweb="tab"] {
            height: 42px;
            border-radius: 11px;
            padding-left: 1rem;
            padding-right: 1rem;
            color: #755866;
            font-weight: 650;
        }

        .stTabs [aria-selected="true"] {
            color: white !important;
            background:
                linear-gradient(
                    135deg,
                    #8d4a6b,
                    #bf6386
                ) !important;
        }

        .stTabs [data-baseweb="tab-highlight"] {
            display: none;
        }

        @media (max-width: 800px) {
            .block-container {
                padding-top: 5rem !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }

            .stTabs [data-baseweb="tab-list"] {
                overflow-x: auto;
                flex-wrap: nowrap;
            }
        }
    </style>
    """
)


# =========================================================
# UI COMPONENTS
# =========================================================

def render_hero():
    st.html(
        """
        <div style="
            position: relative;
            overflow: hidden;
            padding: 32px;
            border-radius: 28px;
            border: 1px solid rgba(156,85,120,0.13);
            background:
                linear-gradient(
                    135deg,
                    rgba(255,255,255,0.97),
                    rgba(255,241,246,0.92)
                );
            box-shadow:
                0 18px 42px rgba(110,62,84,0.10);
            margin-bottom: 14px;
        ">

            <div style="
                position: absolute;
                width: 240px;
                height: 240px;
                border-radius: 50%;
                right: -75px;
                top: -78px;
                background:
                    linear-gradient(
                        135deg,
                        rgba(226,148,177,0.42),
                        rgba(205,185,237,0.48)
                    );
            "></div>

            <div style="
                position: relative;
                z-index: 2;
                display: inline-block;
                padding: 7px 12px;
                border-radius: 999px;
                background: rgba(156,85,120,0.09);
                color: #8e4e6e;
                font-size: 12px;
                font-weight: 800;
                margin-bottom: 16px;
            ">
                🌷 OPERATIONS PORTFOLIO
            </div>

            <div style="
                position: relative;
                z-index: 2;
                max-width: 850px;
                color: #3d2f38;
                font-size: clamp(38px, 6vw, 62px);
                line-height: 1.03;
                font-weight: 800;
                letter-spacing: -2px;
            ">
                Administrative Data Quality Monitor
            </div>

            <div style="
                position: relative;
                z-index: 2;
                max-width: 760px;
                margin-top: 17px;
                color: #7f6d77;
                font-size: 16px;
                line-height: 1.7;
            ">
                A simple workspace for checking administrative records,
                spotting incomplete or overdue items,
                and organizing follow-up tasks.
            </div>

            <div style="
                position: relative;
                z-index: 2;
                display: flex;
                flex-wrap: wrap;
                gap: 8px;
                margin-top: 18px;
            ">

                <span style="
                    padding: 7px 11px;
                    border-radius: 999px;
                    background: white;
                    border: 1px solid #eadfe4;
                    color: #684f5b;
                    font-size: 13px;
                    font-weight: 650;
                ">
                    Admin operations
                </span>

                <span style="
                    padding: 7px 11px;
                    border-radius: 999px;
                    background: white;
                    border: 1px solid #eadfe4;
                    color: #684f5b;
                    font-size: 13px;
                    font-weight: 650;
                ">
                    Data quality
                </span>

                <span style="
                    padding: 7px 11px;
                    border-radius: 999px;
                    background: white;
                    border: 1px solid #eadfe4;
                    color: #684f5b;
                    font-size: 13px;
                    font-weight: 650;
                ">
                    Workload monitoring
                </span>

                <span style="
                    padding: 7px 11px;
                    border-radius: 999px;
                    background: white;
                    border: 1px solid #eadfe4;
                    color: #684f5b;
                    font-size: 13px;
                    font-weight: 650;
                ">
                    Python + Streamlit
                </span>

            </div>
        </div>
        """
    )


def render_section(kicker, title, description):
    st.html(
        f"""
        <div style="
            margin-top: 25px;
            margin-bottom: 13px;
        ">
            <div style="
                color: #b15d82;
                font-size: 12px;
                font-weight: 800;
                letter-spacing: 1.4px;
                margin-bottom: 7px;
            ">
                {kicker.upper()}
            </div>

            <div style="
                color: #3d2f38;
                font-size: 31px;
                line-height: 1.15;
                font-weight: 800;
                letter-spacing: -0.8px;
            ">
                {title}
            </div>

            <div style="
                margin-top: 8px;
                color: #7f6d77;
                font-size: 15px;
                line-height: 1.65;
                max-width: 850px;
            ">
                {description}
            </div>
        </div>
        """
    )


def render_workflow():
    st.html(
        """
        <div style="
            display: grid;
            grid-template-columns:
                repeat(auto-fit, minmax(210px, 1fr));
            gap: 12px;
            margin: 16px 0 24px 0;
        ">

            <div style="
                padding: 18px;
                border-radius: 20px;
                background: rgba(255,255,255,0.88);
                border: 1px solid #eadfe4;
                box-shadow: 0 8px 22px rgba(104,64,82,0.06);
            ">
                <div style="color:#b45d82;font-size:12px;font-weight:800;">01</div>
                <div style="margin-top:7px;color:#3d2f38;font-size:16px;font-weight:750;">
                    Load records
                </div>
                <div style="margin-top:5px;color:#7f6d77;font-size:13px;line-height:1.5;">
                    Use the sample data or upload another file.
                </div>
            </div>

            <div style="
                padding: 18px;
                border-radius: 20px;
                background: rgba(255,255,255,0.88);
                border: 1px solid #eadfe4;
                box-shadow: 0 8px 22px rgba(104,64,82,0.06);
            ">
                <div style="color:#b45d82;font-size:12px;font-weight:800;">02</div>
                <div style="margin-top:7px;color:#3d2f38;font-size:16px;font-weight:750;">
                    Check quality
                </div>
                <div style="margin-top:5px;color:#7f6d77;font-size:13px;line-height:1.5;">
                    Find missing, duplicate, overdue, and inconsistent records.
                </div>
            </div>

            <div style="
                padding: 18px;
                border-radius: 20px;
                background: rgba(255,255,255,0.88);
                border: 1px solid #eadfe4;
                box-shadow: 0 8px 22px rgba(104,64,82,0.06);
            ">
                <div style="color:#b45d82;font-size:12px;font-weight:800;">03</div>
                <div style="margin-top:7px;color:#3d2f38;font-size:16px;font-weight:750;">
                    Prioritize follow-up
                </div>
                <div style="margin-top:5px;color:#7f6d77;font-size:13px;line-height:1.5;">
                    Focus on records that need action first.
                </div>
            </div>

            <div style="
                padding: 18px;
                border-radius: 20px;
                background: rgba(255,255,255,0.88);
                border: 1px solid #eadfe4;
                box-shadow: 0 8px 22px rgba(104,64,82,0.06);
            ">
                <div style="color:#b45d82;font-size:12px;font-weight:800;">04</div>
                <div style="margin-top:7px;color:#3d2f38;font-size:16px;font-weight:750;">
                    Export results
                </div>
                <div style="margin-top:5px;color:#7f6d77;font-size:13px;line-height:1.5;">
                    Download reviewed records as CSV.
                </div>
            </div>

        </div>
        """
    )


def make_metric_card(label, value, caption, accent):
    return f"""
        <div style="
            position: relative;
            overflow: hidden;
            min-height: 118px;
            padding: 18px;
            border-radius: 21px;
            background: rgba(255,255,255,0.91);
            border: 1px solid #eadfe4;
            box-shadow: 0 9px 22px rgba(104,64,82,0.065);
        ">

            <div style="
                position: absolute;
                width: 64px;
                height: 64px;
                border-radius: 50%;
                right: -18px;
                top: -18px;
                background: {accent};
                opacity: 0.55;
            "></div>

            <div style="
                position: relative;
                z-index: 2;
                color: #8b7580;
                font-size: 12px;
                font-weight: 650;
            ">
                {label}
            </div>

            <div style="
                position: relative;
                z-index: 2;
                margin-top: 8px;
                color: #7b4061;
                font-size: 31px;
                line-height: 1;
                font-weight: 800;
            ">
                {value}
            </div>

            <div style="
                position: relative;
                z-index: 2;
                margin-top: 9px;
                color: #9a8590;
                font-size: 11px;
            ">
                {caption}
            </div>

        </div>
    """


def render_bar(label, value, maximum):
    width = 0 if maximum == 0 else value / maximum * 100

    st.html(
        f"""
        <div style="
            padding: 16px;
            border-radius: 18px;
            border: 1px solid #eadfe4;
            background: rgba(255,255,255,0.88);
            margin-bottom: 9px;
            box-shadow: 0 7px 18px rgba(104,64,82,0.045);
        ">
            <div style="
                display: flex;
                justify-content: space-between;
                gap: 10px;
                margin-bottom: 8px;
            ">
                <div style="
                    color: #49363f;
                    font-size: 13px;
                    font-weight: 700;
                ">
                    {label}
                </div>

                <div style="
                    color: #934c70;
                    font-size: 13px;
                    font-weight: 800;
                ">
                    {value:,}
                </div>
            </div>

            <div style="
                height: 9px;
                border-radius: 999px;
                background: #f0e6eb;
                overflow: hidden;
            ">
                <div style="
                    width: {width:.1f}%;
                    height: 100%;
                    border-radius: 999px;
                    background:
                        linear-gradient(
                            90deg,
                            #ad587d,
                            #e58eab,
                            #ccb3ec
                        );
                "></div>
            </div>
        </div>
        """
    )


# =========================================================
# SAMPLE DATA
# =========================================================

@st.cache_data
def build_sample_data(total_rows=1500):

    random.seed(72)

    document_types = [
        "Purchase Request",
        "Travel Request",
        "Employee Document",
        "Invoice",
        "Internal Memo",
        "Meeting Document",
        "Asset Record",
        "Vendor Document",
    ]

    departments = [
        "General Affairs",
        "Finance",
        "Human Resources",
        "Operations",
        "Procurement",
        "Administration",
    ]

    pics = [
        "Alya",
        "Nadia",
        "Rani",
        "Dina",
        "Salsa",
        "Mira",
        "Intan",
        "Tasya",
    ]

    statuses = [
        "New",
        "In Review",
        "Waiting",
        "Completed",
    ]

    today = datetime.now()
    start_date = today - timedelta(days=250)

    rows = []
    record_pool = []

    for i in range(1, total_rows + 1):

        document_id = f"ADM-{i:05d}"
        record_pool.append(document_id)

        document_type = random.choice(document_types)
        department = random.choice(departments)
        pic = random.choice(pics)

        submission_date = (
            start_date
            + timedelta(days=random.randint(0, 240))
        )

        due_date = (
            submission_date
            + timedelta(days=random.randint(3, 25))
        )

        status = random.choices(
            statuses,
            weights=[10, 24, 16, 50],
        )[0]

        if status == "Completed":
            completion_date = (
                submission_date
                + timedelta(days=random.randint(1, 22))
            )
        else:
            completion_date = pd.NaT

        applicant = (
            f"Requester {random.randint(100, 999)}"
        )

        notes = random.choice(
            [
                "Complete",
                "Waiting for confirmation",
                "Need supporting document",
                "Follow up required",
                "Reviewed",
                "",
            ]
        )

        issue_roll = random.random()

        if issue_roll < 0.025 and i > 30:
            document_id = random.choice(
                record_pool[:-1]
            )

        elif issue_roll < 0.050:
            pic = None

        elif issue_roll < 0.075:
            department = None

        elif issue_roll < 0.100:
            document_type = None

        elif issue_roll < 0.125:
            applicant = None

        elif issue_roll < 0.150:
            status = "Completed"
            completion_date = pd.NaT

        elif issue_roll < 0.175:
            status = "In Review"
            completion_date = (
                submission_date
                + timedelta(days=random.randint(2, 15))
            )

        elif issue_roll < 0.210:
            due_date = (
                today
                - timedelta(days=random.randint(1, 50))
            )
            status = random.choice(
                ["New", "In Review", "Waiting"]
            )

        rows.append(
            {
                "document_id":
                    document_id,

                "requester":
                    applicant,

                "document_type":
                    document_type,

                "department":
                    department,

                "pic":
                    pic,

                "submission_date":
                    submission_date,

                "due_date":
                    due_date,

                "status":
                    status,

                "completion_date":
                    completion_date,

                "notes":
                    notes,
            }
        )

    return pd.DataFrame(rows)


# =========================================================
# FILE INPUT
# =========================================================

REQUIRED_COLUMNS = [
    "document_id",
    "requester",
    "document_type",
    "department",
    "pic",
    "submission_date",
    "due_date",
    "status",
    "completion_date",
    "notes",
]


def read_uploaded_file(uploaded_file):

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".csv"):
        return pd.read_csv(uploaded_file)

    if (
        file_name.endswith(".xlsx")
        or file_name.endswith(".xls")
    ):
        return pd.read_excel(uploaded_file)

    raise ValueError(
        "Please upload a CSV or Excel file."
    )


# =========================================================
# QUALITY CHECK ENGINE
# =========================================================

def review_admin_data(df):

    checked = df.copy()

    for column in [
        "submission_date",
        "due_date",
        "completion_date",
    ]:
        checked[column] = pd.to_datetime(
            checked[column],
            errors="coerce",
        )

    today = pd.Timestamp.today().normalize()

    duplicate_mask = (
        checked["document_id"]
        .astype("string")
        .duplicated(keep=False)
        &
        checked["document_id"].notna()
    )

    required_fields = [
        "document_id",
        "requester",
        "document_type",
        "department",
        "pic",
        "submission_date",
        "due_date",
        "status",
    ]

    rank = {
        "Low": 0,
        "Medium": 1,
        "High": 2,
        "Critical": 3,
    }

    review_statuses = []
    priorities = []
    issue_notes = []

    for index, row in checked.iterrows():

        issues = []
        current_priority = "Low"

        def upgrade(target):
            nonlocal current_priority

            if (
                rank[target]
                >
                rank[current_priority]
            ):
                current_priority = target

        missing = []

        for field in required_fields:
            value = row.get(field)

            if (
                pd.isna(value)
                or str(value).strip() == ""
            ):
                missing.append(field)

        if missing:
            issues.append(
                "Missing "
                + ", ".join(missing)
            )
            upgrade("High")

        if duplicate_mask.loc[index]:
            issues.append(
                "Duplicate document ID"
            )
            upgrade("High")

        status = str(
            row.get("status", "")
        ).strip()

        due_date = row.get("due_date")
        completion_date = row.get(
            "completion_date"
        )
        submission_date = row.get(
            "submission_date"
        )

        if (
            pd.notna(due_date)
            and due_date < today
            and status.lower() != "completed"
        ):
            issues.append(
                "Overdue"
            )
            upgrade("Critical")

        if (
            status.lower() == "completed"
            and pd.isna(completion_date)
        ):
            issues.append(
                "Completed status without completion date"
            )
            upgrade("High")

        if (
            status.lower() != "completed"
            and pd.notna(completion_date)
        ):
            issues.append(
                "Completion date exists but status is not Completed"
            )
            upgrade("High")

        if (
            pd.notna(submission_date)
            and status.lower() in {
                "new",
                "in review",
                "waiting",
            }
            and (
                today - submission_date
            ).days > 30
        ):
            issues.append(
                "Open for more than 30 days"
            )
            upgrade("Medium")

        if issues:
            review_statuses.append(
                "Need Review"
            )
            issue_notes.append(
                "; ".join(
                    dict.fromkeys(issues)
                )
            )
        else:
            review_statuses.append(
                "Clear"
            )
            issue_notes.append(
                "No issue found"
            )

        priorities.append(
            current_priority
        )

    checked["review_status"] = (
        review_statuses
    )
    checked["priority"] = (
        priorities
    )
    checked["issue_found"] = (
        issue_notes
    )

    return checked


# =========================================================
# APP START
# =========================================================

render_hero()

st.caption(
    "This app uses synthetic administrative records for portfolio purposes."
)


render_section(
    "Workflow",
    "From raw admin records to a follow-up list",
    (
        "The app checks common administrative data issues, "
        "then organizes the records that may need attention."
    ),
)

render_workflow()


# =========================================================
# INPUT
# =========================================================

render_section(
    "Input",
    "Choose your data",
    (
        "Use the built in sample dataset or upload another file "
        "with the same column structure."
    ),
)


source = st.radio(
    "Data source",
    [
        "Use sample data",
        "Upload a file",
    ],
    horizontal=True,
    label_visibility="collapsed",
)


data = None


if source == "Use sample data":

    data = build_sample_data()

    st.success(
        f"Sample data ready. "
        f"{len(data):,} records loaded."
    )


else:

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel",
        type=[
            "csv",
            "xlsx",
            "xls",
        ],
    )

    if uploaded_file is not None:

        try:

            data = read_uploaded_file(
                uploaded_file
            )

            st.success(
                f"{uploaded_file.name} loaded."
            )

        except Exception as error:

            st.error(
                str(error)
            )


if data is None:

    st.info(
        "Choose the sample data "
        "or upload a file to continue."
    )

    st.stop()


# =========================================================
# COLUMN CHECK
# =========================================================

missing_columns = [
    column
    for column in REQUIRED_COLUMNS
    if column not in data.columns
]


if missing_columns:

    st.error(
        "Missing required columns: "
        + ", ".join(
            missing_columns
        )
    )

    st.stop()


# =========================================================
# PREVIEW
# =========================================================

preview_left, preview_right = (
    st.columns(
        [1.35, 1]
    )
)


with preview_left:

    st.subheader(
        "Quick preview"
    )

    st.dataframe(
        data.head(8),
        use_container_width=True,
        hide_index=True,
        height=310,
    )


with preview_right:

    st.subheader(
        "Checks included"
    )

    st.markdown(
        """
        Missing required fields  
        Duplicate document IDs  
        Overdue open records  
        Status and completion-date mismatch  
        Open records older than 30 days  
        PIC and department completeness
        """
    )

    st.caption(
        "The output is a portfolio simulation "
        "and not an official administrative assessment."
    )


st.write("")


# =========================================================
# CHECK BUTTON
# =========================================================

if st.button(
    "Check records",
    use_container_width=True,
):

    st.session_state[
        "admin_checked_results"
    ] = review_admin_data(
        data
    )


if (
    "admin_checked_results"
    not in st.session_state
):

    st.stop()


result = (
    st.session_state[
        "admin_checked_results"
    ].copy()
)


# =========================================================
# SUMMARY
# =========================================================

total_records = len(result)

clear_records = int(
    (
        result["review_status"]
        == "Clear"
    ).sum()
)

review_records = int(
    (
        result["review_status"]
        == "Need Review"
    ).sum()
)

critical_records = int(
    (
        result["priority"]
        == "Critical"
    ).sum()
)

overdue_records = int(
    result[
        "issue_found"
    ]
    .str.contains(
        "Overdue",
        na=False,
    )
    .sum()
)

health_score = (
    clear_records
    / total_records
    * 100
    if total_records > 0
    else 0
)


render_section(
    "Output",
    "Administrative health summary",
    (
        "A quick view of data completeness, follow-up workload, "
        "and the records that may need attention first."
    ),
)


cards = (
    """
    <div style="
        display: grid;
        grid-template-columns:
            repeat(auto-fit, minmax(170px, 1fr));
        gap: 11px;
        margin: 16px 0 22px 0;
    ">
    """
    +
    make_metric_card(
        "Records checked",
        f"{total_records:,}",
        "All loaded records",
        "#f6c5d6",
    )
    +
    make_metric_card(
        "Clear",
        f"{clear_records:,}",
        "No issue detected",
        "#d9d2f3",
    )
    +
    make_metric_card(
        "Need review",
        f"{review_records:,}",
        "At least one issue",
        "#f6cbb7",
    )
    +
    make_metric_card(
        "Health score",
        f"{health_score:.1f}%",
        "Share of clear records",
        "#f2bed0",
    )
    +
    make_metric_card(
        "Overdue",
        f"{overdue_records:,}",
        "Open past due date",
        "#dabfea",
    )
    +
    "</div>"
)

st.html(cards)


# =========================================================
# TABS
# =========================================================

overview_tab, queue_tab, workload_tab, all_tab = (
    st.tabs(
        [
            "Overview",
            "Follow-up queue",
            "PIC workload",
            "All records",
        ]
    )
)


# =========================================================
# OVERVIEW
# =========================================================

with overview_tab:

    left, right = st.columns(2)


    with left:

        st.subheader(
            "Priority mix"
        )

        priority_counts = (
            result["priority"]
            .value_counts()
            .reindex(
                [
                    "Critical",
                    "High",
                    "Medium",
                    "Low",
                ],
                fill_value=0,
            )
        )

        maximum = int(
            priority_counts.max()
        )

        for label, value in (
            priority_counts.items()
        ):

            render_bar(
                label,
                int(value),
                maximum,
            )


    with right:

        st.subheader(
            "Common issues"
        )

        issue_counts = (
            result.loc[
                result[
                    "review_status"
                ]
                == "Need Review",
                "issue_found",
            ]
            .value_counts()
            .head(6)
        )

        if issue_counts.empty:

            st.success(
                "No issues found."
            )

        else:

            maximum_issue = int(
                issue_counts.max()
            )

            for label, value in (
                issue_counts.items()
            ):

                render_bar(
                    label,
                    int(value),
                    maximum_issue,
                )


# =========================================================
# FOLLOW-UP QUEUE
# =========================================================

with queue_tab:

    st.subheader(
        "Records that need follow-up"
    )

    review_data = (
        result[
            result[
                "review_status"
            ]
            == "Need Review"
        ]
        .copy()
    )


    filter_one, filter_two, filter_three = (
        st.columns(3)
    )


    with filter_one:

        priority_filter = (
            st.multiselect(
                "Priority",
                [
                    "Critical",
                    "High",
                    "Medium",
                    "Low",
                ],
                default=[
                    "Critical",
                    "High",
                    "Medium",
                ],
            )
        )


    with filter_two:

        department_options = sorted(
            review_data[
                "department"
            ]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        department_filter = (
            st.multiselect(
                "Department",
                department_options,
            )
        )


    with filter_three:

        pic_options = sorted(
            review_data[
                "pic"
            ]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        pic_filter = (
            st.multiselect(
                "PIC",
                pic_options,
            )
        )


    filtered = (
        review_data.copy()
    )


    if priority_filter:

        filtered = filtered[
            filtered[
                "priority"
            ]
            .isin(
                priority_filter
            )
        ]


    if department_filter:

        filtered = filtered[
            filtered[
                "department"
            ]
            .astype(str)
            .isin(
                department_filter
            )
        ]


    if pic_filter:

        filtered = filtered[
            filtered[
                "pic"
            ]
            .astype(str)
            .isin(
                pic_filter
            )
        ]


    queue_columns = [
        "document_id",
        "requester",
        "document_type",
        "department",
        "pic",
        "submission_date",
        "due_date",
        "status",
        "priority",
        "issue_found",
    ]


    st.dataframe(
        filtered[
            queue_columns
        ],
        use_container_width=True,
        hide_index=True,
        height=520,
    )


    st.caption(
        f"{len(filtered):,} records shown."
    )


# =========================================================
# PIC WORKLOAD
# =========================================================

with workload_tab:

    st.subheader(
        "PIC workload"
    )

    workload = (
        result[
            result[
                "status"
            ]
            .astype(str)
            .str.lower()
            != "completed"
        ]
        .groupby(
            "pic",
            dropna=False,
        )
        .size()
        .sort_values(
            ascending=False
        )
    )

    workload_table = (
        workload
        .rename(
            "open_records"
        )
        .reset_index()
    )


    st.dataframe(
        workload_table,
        use_container_width=True,
        hide_index=True,
        height=360,
    )


    max_workload = (
        int(workload.max())
        if len(workload) > 0
        else 0
    )

    for label, value in (
        workload.head(8).items()
    ):

        render_bar(
            str(label),
            int(value),
            max_workload,
        )


# =========================================================
# ALL RECORDS
# =========================================================

with all_tab:

    st.subheader(
        "Checked records"
    )

    st.dataframe(
        result,
        use_container_width=True,
        hide_index=True,
        height=540,
    )


    csv_data = (
        result
        .to_csv(
            index=False
        )
        .encode(
            "utf-8-sig"
        )
    )


    st.download_button(
        "Download checked data",
        data=csv_data,
        file_name=
            "administrative_quality_results.csv",
        mime="text/csv",
        use_container_width=True,
    )


# =========================================================
# FOOTER
# =========================================================

st.write("")

st.caption(
    "Portfolio project using synthetic administrative data."
)
