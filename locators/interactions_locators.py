from selenium.webdriver.common.by import By


class InteractionsPageLocators():
    TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    LIST_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')
    TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    GRID_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')

class SelectablePageLocators():
    TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    LIST_ITEM = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item list-group-item-action"]')
    LIST_ITEM_ACTIVE = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item active list-group-item-action"]')

    TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    GRID_ITEM = (By.CSS_SELECTOR, 'li[class="list-group-item list-group-item-action"]')
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, 'li[class="list-group-item active list-group-item-action"]')

class DroppablePageLocators():
    # Simple

    SIMPLE_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-simple']")
    DRAG_ME_SIMPLE = (By.CSS_SELECTOR, "div[id='draggable']")
    DROP_HERE_SIMPLE = (By.CSS_SELECTOR, "div[id='simpleDropContainer'] div[id='droppable']")

    # Accept
    ACCEPT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-accept']")
    ACCEPTABLE = (By.CSS_SELECTOR, "div[id='acceptable']")
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, "div[id='notAcceptable']")
    DROP_HERE_ACCEPTABLE = (By.CSS_SELECTOR, "div[id='acceptDropContainer'] div[id='droppable']")

    # Prevent Propogation

    PREVENT_PROPOGATION_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-preventPropogation']")
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, "div[id='dragBox']")
    NOT_GREEDY_DROPBOX_TEXT = (By.CSS_SELECTOR, "div[id='notGreedyDropBox'] p:nth-child(1)")
    NOT_GREEDY_INNER = (By.CSS_SELECTOR, "div[id='notGreedyInnerDropBox']")
    GREEDY_DROPBOX_TEXT = (By.CSS_SELECTOR, "div[id='greedyDropBox'] p:nth-child(1)")
    GREEDY_INNER = (By.CSS_SELECTOR, "div[id='greedyDropBoxInner']")

    # Revert Draggable

    REVERT_DRAGGABLE_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-revertable']")
    WILL_REVERT = (By.CSS_SELECTOR, "div[id='revertable']")
    NOT_REVERT = (By.CSS_SELECTOR, "div[id='notRevertable']")
    DROP_HERE_DRAGGABLE = (By.CSS_SELECTOR, "div[id='revertableDropContainer'] div[id='droppable']")

class DraggablePageLocators:
    # Simple Drag
    SIMPLE_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-simple']")
    DRAG_ME = (By.CSS_SELECTOR, "div[id='dragBox']")

    # Axis Restricted
    AXIS_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-axisRestriction']")
    ONLY_X = (By.CSS_SELECTOR, "div[id='restrictedX']")
    ONLY_Y = (By.CSS_SELECTOR, "div[id='restrictedY']")
